from collections import deque
import datetime
import websocket
import json
import logging
import os
from fx_py_sdk import constants
import threading
from fx_py_sdk.model.block import *
from fx_py_sdk.model.model import *
from fx_py_sdk.model.crud import *
from fx_py_sdk.fx_rpc.rpc import *
from google.protobuf.timestamp_pb2 import Timestamp
from sqlalchemy import and_
from fx_py_sdk.grpc_client import GRPCClient
import traceback
import time
from fx_py_sdk.notify_service import send_mail
from fx_py_sdk.scan_block import ScanBlock, ScanBlockBase

reconnect_block_count = 0
reconnect_tx_count = 0
tm_event_NewBlock = "tm.event='NewBlock'"
tm_event_Tx = "tm.event='Tx'"

history_file_prefix = 'fxdex_blocks'

class ScanManager:
    def __init__(self, rpc_page_size=5, rpc_max_retries=3):
        self.scan = ScanBlock()

        self.ws_scan = WebsocketScan(self)
        self.rpc_scan = RpcScan(self,
                                page_size=rpc_page_size,
                                rpc_max_retries=rpc_max_retries)
                                
        self.account_scan = AccountScan(self, update_interval_seconds=60)
        self.error_scan = ErrorScan(self,
                                    update_interval_seconds=1,
                                    rpc_max_retries=rpc_max_retries)    # rpc only, ws has no code

class RpcScan:
    """use rpc connect fxdex, scan block event"""

    def __init__(self, scan_manager: ScanManager, page_size=10, rpc_max_retries=3):
        self.manager = scan_manager
        self.scan = ScanBlock()
        self.page_size = page_size

        self.rpc_url = constants.Network.get_rpc_url()
        self.rpc_client = HttpRpcClient(self.rpc_url, max_retries=rpc_max_retries)

        self.process_block_threaded()

    def process_block_threaded(self):
        threading.Thread(target=self.process_block).start()

    def process_block(self):
        start_block = None

        while True:
            """parse block data"""

            abci_info = self.rpc_client.get_abci_info()
            latest_block_height = int(
                abci_info["response"]["last_block_height"])

            """get last sync block height from sql"""
            if not start_block:
                start_block = int(os.environ.get('START_BLOCK', '1'))

            block_heights = [blk_ht for blk_ht, in (self.scan.crud.session.query(Block)
                                                                         .filter(Block.height >= start_block)
                                                                         .with_entities(Block.height)
                                                                         .order_by(Block.height))]
            missing_blocks = list(sorted(
                set(range(start_block, latest_block_height+1)).difference(set(block_heights))
            ))

            if not missing_blocks:  # use WebSockets if fully synced
                logging.info(
                    'Synced with latest block. Switching to WebSockets...')
                self.manager.ws_scan.rpc_ready = True
                return
            
            first_block_height = missing_blocks[0]  # min
            last_block_height = missing_blocks[-1]  # max
            logging.info("Rpc scan from %d to %d (%d blocks)",
                         first_block_height, last_block_height, len(missing_blocks))

            def get_block_results(block_height, results_arr):
                while True:
                    try:
                        block_result = self.rpc_client.get_block_results(block_height)
                        block_rpc = self.rpc_client.get_block(block_height)
                        results_arr.append((block_result, block_rpc))
                        return
                    except Exception as ex:
                        logging.error(f'Error retrieving block: {ex}')
                        time.sleep(10)

            data = {}

            for i in range(0, len(missing_blocks), self.page_size):
                if i > 0 and i % 10000 <= self.page_size:
                    logging.info(str(i))

                thread_list = []
                results = []

                next_chunk = missing_blocks[i:i+self.page_size]
                for block_height in next_chunk:
                    thread_list.append(threading.Thread(target=get_block_results, args=(block_height, results)))

                for t in thread_list:
                    t.start()
                for t in thread_list:
                    t.join()

                # process sequentially
                for block_result, block_rpc in sorted(results, key=lambda x: x[0]['height']):
                    block_height = int(block_result['height'])
                    block_time = block_rpc[BlockResponse.BLOCK][BlockResponse.HEADER][BlockResponse.Time]

                    timestamp = Timestamp()
                    timestamp.FromJsonString(block_time),
                    block_datetime = datetime.datetime.utcfromtimestamp(timestamp.ToSeconds())

                    # If txs_results is not None, process each tx_event
                    if block_result[BlockResponse.Txs_results] is not None:
                        for tx_result in block_result[BlockResponse.Txs_results]:
                            tx_events = tx_result[BlockResponse.EVENTS]
                            self.scan.process_tx_events(tx_events, block_height)
                    # Else update block height in any case
                    else:
                        block = Block(height=block_height, time=block_datetime, tx_events_processed=True)
                        self.scan.process_block_height(block)

                    if block_result[BlockResponse.Begin_block_events] is not None:
                        self.scan.process_begin_block(
                            block_result[BlockResponse.Begin_block_events], block_height)

                    self.scan.realized_positions[block_height] = deque()
                    if block_result[BlockResponse.End_block_events] is not None:
                        self.scan.process_end_block(
                            block_result[BlockResponse.End_block_events], block_height)

                    self.scan.process_best_bid_ask(block_height, True)
                    self.scan.process_cumulative_realized_pnl(block_height)

                    # Update latest block on chain
                    block = Block(height=block_height, time=block_datetime, block_processed=True)
                    self.scan.process_block_height(block)

            # Read the block directly after all missing blocks previously acquired
            start_block = last_block_height + 1

class WebsocketScan:
    """use websocket connect fxdex, scan block event"""

    def __init__(self, scan_manager: ScanManager=None, subscribe_events: Iterable=None, scan: ScanBlockBase = None):
        self.manager = scan_manager
        self.scan: ScanBlockBase = scan or ScanBlock()

        self.wss_url = constants.Network.get_ws_url()

        self.ws_block = None
        self.rpc_ready = False

        self.subscribe_events = subscribe_events or [tm_event_NewBlock, tm_event_Tx]
        threading.Thread(target=self.subscribe_block).start()

    def _get_ws_endpoint_url(self):
        return f"{self.wss_url}websocket"

    def _handle_exception(self, error, send_email=True):
        was_ready = self.rpc_ready
        self.rpc_ready = False

        title = f'WS error in handling message: {str(error)} (Blk Ht: {self.scan.max_block_height})'
        exception_traceback = traceback.format_exc()
        logging.warning(title)
        logging.warning(exception_traceback)
        if was_ready:
            send_mail(title, exception_traceback, recipients='matthew.ang@pundix.com')

        global reconnect_block_count
        print("websocket caught: ", error)
        if (isinstance(error, ConnectionRefusedError) or
            isinstance(error, ConnectionResetError) or
            isinstance(error, websocket._exceptions.WebSocketConnectionClosedException)):

            time.sleep(1.0 * 2**reconnect_block_count)   # wait a while so we don't spam the server
            logging.info("正在尝试第 %d 次重连" % reconnect_block_count)
            reconnect_block_count += 1

            """
            if we were processing WS data before, then we need to resume RPC
            else, RPC is probably already running - we don't need to do anything extra
            """
            if was_ready and self.manager and isinstance(self.scan, ScanBlock):
                # reinstate connection (in case of idle-in-transaction timeout)
                self.manager.rpc_scan.scan.crud.init_session()
                # delete all data from the most recent block height with incomplete data
                self.manager.rpc_scan.scan.crud.delete_data_from_lowest_incomplete_height()
                # process RPC data sequentially
                self.manager.rpc_scan.process_block_threaded()

            """reinstate websocket connection"""
            self.subscribe_block()
        else:
            print("error: ", error)

    def on_error(self, error):
        self._handle_exception(error)

    def on_message(self, message):        
        if self.manager and not self.rpc_ready:
            return

        global reconnect_block_count
        reconnect_block_count = 0
        msg = json.loads(message)

        try:
            if str(msg[BlockResponse.RESULT]) != '{}':
                if msg[BlockResponse.RESULT][BlockResponse.QUERY] == tm_event_Tx:
                    if BlockResponse.RESULT not in msg:
                        logging.debug(f"result not in message yet {msg}")
                        return
                    if BlockResponse.DATA not in msg[BlockResponse.RESULT]:
                        logging.debug(f"data not in message yet {msg}")
                        return
                    if BlockResponse.VALUE not in msg[BlockResponse.RESULT][BlockResponse.DATA]:
                        logging.debug(f"value not in message yet {msg}")
                        return
                    if BlockResponse.TxResult not in msg[BlockResponse.RESULT][BlockResponse.DATA][
                        BlockResponse.VALUE]:
                        logging.debug(f"tx_result not in message yet {msg}")
                        return
                    
                    tx_result = msg[BlockResponse.RESULT][BlockResponse.DATA][BlockResponse.VALUE][
                        BlockResponse.TxResult]
                    if BlockResponse.EVENTS not in tx_result[BlockResponse.RESULT]:
                        logging.debug(f"events not in tx_result yet {msg}")
                        return

                    block_height = int(tx_result[BlockResponse.HEIGHT])
                    if tx_result is not None and BlockResponse.EVENTS in tx_result[BlockResponse.RESULT]:
                        tx_events = tx_result[BlockResponse.RESULT][BlockResponse.EVENTS]
                    else:
                        tx_events = []
                    self.scan.process_tx_events(tx_events, block_height)
                elif msg[BlockResponse.RESULT][BlockResponse.QUERY] == tm_event_NewBlock:
                    self.scan.process_block(msg)
        except Exception as ex:
            self._handle_exception(ex)

    def on_open(self):
        logging.info("connection to fxdex...")
        for event in self.subscribe_events:
            data = {
                "jsonrpc": "2.0",
                "method": "subscribe",
                "params": [event],
                "id": 1
            }
            data = json.dumps(data).encode()
            self.ws_block.send(data)

    def on_close(self):
        logging.info("connection to fxdex websocket is closed")

    def subscribe_block(self):
        websocket.enableTrace(False)    # prevent debug messages
        logging.info(self._get_ws_endpoint_url())
        self.ws_block = websocket.WebSocketApp(self._get_ws_endpoint_url(),
                                               on_message=self.on_message,
                                               on_error=self.on_error,
                                               on_close=self.on_close,
                                               on_open=self.on_open)
        try:
            self.ws_block.run_forever()
        except KeyboardInterrupt:
            self.ws_block.close()
        except:
            self.ws_block.close()

class AccountScan:
    def __init__(self, scan_manager: ScanManager, update_interval_seconds=60):
        self.manager = scan_manager
        self.owners = None
        self.last_updated = None

        self.client = scan_manager.scan.client or GRPCClient(constants.Network.get_grpc_url())
        self.update_interval = update_interval_seconds

        threading.Thread(target=self.update_account_balances_looped).start()

    def update_account_balances(self):
        logging.info('Updating account balances...')
        now = datetime.datetime.utcnow()

        if not self.owners or (now - self.last_updated) > datetime.timedelta(seconds=self.update_interval*9.5):            
            query_result = self.manager.scan.crud.session.execute('SELECT DISTINCT owner FROM trade;').fetchall()
            self.owners = [res[0] for res in query_result]
            self.last_updated = now

        if not self.owners:
            return

        all_balances = []

        batch_time = datetime.datetime.utcnow()
        for owner in self.owners:
            time_updated = datetime.datetime.utcnow()
            balances = self.client.query_all_balances(owner)
            
            for symbol, balance_amount in balances.items():
                bal = Balance(owner=owner, token=symbol, amount=balance_amount, batch_time=batch_time, time=time_updated)
                all_balances.append(bal)
        
        self.client.crud.insert_many(all_balances)

    def update_account_balances_looped(self):
        while True:
            try:
                self.update_account_balances()
            except Exception as ex:
                logging.error(f'Error updating balances: {ex}')
                self.client = GRPCClient(constants.Network.get_grpc_url())  # refresh client
            finally:
                time.sleep(self.update_interval)

class ErrorScan:
    def __init__(self, scan_manager: ScanManager, update_interval_seconds=1, rpc_max_retries=3):
        self.manager = scan_manager
        self.owners = None
        self.last_updated = None

        self.scan = ScanBlock()
        self.crud = self.scan.client.crud
        self.update_interval = update_interval_seconds

        self.rpc_url = constants.Network.get_rpc_url()
        self.rpc_max_retries = rpc_max_retries

        threading.Thread(target=self.update_error_logs_looped).start()

    def update_error_logs(self):
        max_block_height = self.crud.session.query(func.max(Block.height)).scalar()
        if not max_block_height:
            return  # wait until we at least have a single block
        max_error_height = self.crud.session.query(ErrorLog.height).first()[0]

        for block_height in range(max_error_height+1, max_block_height+1):
            self.rpc_client = HttpRpcClient(self.rpc_url, max_retries=self.rpc_max_retries)
            block_result = self.rpc_client.get_block_results(block_height)

            if block_result[BlockResponse.Txs_results] is not None:
                for tx_result in block_result[BlockResponse.Txs_results]:
                    self.scan.process_tx_errors(tx_result, block_height)

            # Update current error log height
            sql_log = self.crud.session.query(ErrorLog).first()
            error_log = ErrorLog(height=block_height)

            if sql_log:
                self.crud.update(ErrorLog, filter=(ErrorLog.height==sql_log.height),
                                 updic=error_log.to_dict())
            else:
                self.crud.insert(error_log)

    def update_error_logs_looped(self):
        while True:
            self.update_error_logs()

