import base64
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
from decimal import Decimal
import sqlalchemy
from sqlalchemy.orm.exc import NoResultFound
from google.protobuf.timestamp_pb2 import Timestamp
from sqlalchemy import and_
import traceback
import re

reconnect_block_count = 0
reconnect_tx_count = 0
tm_event_NewBlock = "tm.event='NewBlock'"
tm_event_Tx = "tm.event='Tx'"

class RpcScan:
    """use rpc connect fxdex, scan block event"""

    def __init__(self, ws_scan):
        network = os.environ[constants.EnvVar.NETWORK]
        if network == constants.NetworkENV.LOCAL:
            self.rpc_url = constants.Network.LOCAL_RPC
        elif network == constants.NetworkENV.DEVNET:
            self.rpc_url = constants.Network.DEVNET_RPC
        elif network == constants.NetworkENV.TESTNET:
            self.rpc_url = constants.Network.TESTNET_RPC
        elif network == constants.NetworkENV.MAINNET:
            self.rpc_url = constants.Network.MAINNET_RPC
        self.rpc_client = HttpRpcClient(self.rpc_url)
        self.scan = ScanBlock()
        self.ws_scan = ws_scan
        threading.Thread(target=self.process_block).start()

    def process_block(self):
        start_block = None

        while True:
            """parse block data"""
            abci_info = self.rpc_client.get_abci_info()
            latest_block_height = int(abci_info["response"]["last_block_height"])

            """get last sync block height from sql"""
            if not start_block:
                start_block = int(os.environ.get('START_BLOCK', '1'))

            block_heights = [blk_ht for blk_ht, in (self.scan.crud.session.query(Block)
                                                                        .filter(Block.height >= start_block)
                                                                        .with_entities(Block.height)
                                                                        .order_by(Block.height))]
            missing_blocks = list(set(range(start_block, latest_block_height+1)).difference(set(block_heights)))

            """switch to WebSockets when synced with latest block"""
            if not missing_blocks:  # use WebSockets if fully synced
                logging.info('Synced with latest block. Switching to WebSockets...')
                self.ws_scan.rpc_ready = True
                return

            first_block_height = missing_blocks[0]  # min
            last_block_height = missing_blocks[-1]  # max
            logging.info("Rpc scan from %d to %d (%d blocks)", first_block_height, last_block_height, len(missing_blocks))

            """loop through each missing block"""
            for block_height in missing_blocks:
                block_result = self.rpc_client.get_block_results(block_height)

                block_rpc = self.rpc_client.get_block(block_height)
                block_time = block_rpc[BlockResponse.BLOCK][BlockResponse.HEADER][BlockResponse.Time]
                timestamp = Timestamp()
                timestamp.FromJsonString(block_time),
                block_datetime = datetime.datetime.utcfromtimestamp(timestamp.ToSeconds())
                block = Block(height=block_height, time=block_datetime)
                sql_block = self.scan.crud.filterone(Block, Block.height == block_height)
                if sql_block is None:
                    self.scan.crud.insert(block)
                else:
                    self.scan.crud.update(Block, filter=(Block.height == block_height),
                                    updic=block.to_dict())

                if block_result[BlockResponse.Txs_results] is not None:
                    for tx_result in block_result[BlockResponse.Txs_results]:
                        tx_events = tx_result[BlockResponse.EVENTS]
                        self.scan.process_tx(tx_events, block_height)

                if block_result[BlockResponse.Begin_block_events] is not None:
                    self.scan.process_begin_block(block_result[BlockResponse.Begin_block_events], block_height)
                if block_result[BlockResponse.End_block_events] is not None:
                    self.scan.process_end_block(block_result[BlockResponse.End_block_events], block_height)

class WebsocketScan:
    """use websocket connect fxdex, scan block event"""

    def __init__(self):
        network = os.environ[constants.EnvVar.NETWORK]
        if network == constants.NetworkENV.LOCAL:
            self.wss_url = constants.Network.LOCAL_WS
        elif network == constants.NetworkENV.DEVNET:
            self.wss_url = constants.Network.DEVNET_WS
        elif network == constants.NetworkENV.TESTNET:
            self.wss_url = constants.Network.TESTNET_WS
        elif network == constants.NetworkENV.MAINNET:
            self.wss_url = constants.Network.MAINNET_WS
        self.ws_block = None
        self.scan = ScanBlock()
        self.rpc_ready = False
        threading.Thread(target=self.subscribe_block).start()

    def _get_ws_endpoint_url(self):
        return f"{self.wss_url}websocket"

    def on_error(self, error):
        global reconnect_block_count
        print("websocket caught: ", error)
        if type(error) == ConnectionRefusedError or \
                type(error) == ConnectionResetError or \
                type(error) == websocket._exceptions.WebSocketConnectionClosedException:
            print("正在尝试第 %d 次重连" % reconnect_block_count)
            reconnect_block_count += 1
            #if reconnect_block_count < 10:
            self.subscribe_block()
        else:
            print("error: ", error)

    def on_message(self, message):
        if not self.rpc_ready:
            return

        global reconnect_block_count
        reconnect_block_count = 0
        msg = json.loads(message)
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
                tx_events = \
                msg[BlockResponse.RESULT][BlockResponse.DATA][BlockResponse.VALUE][BlockResponse.TxResult][
                    BlockResponse.RESULT][BlockResponse.EVENTS]
                block_height = \
                msg[BlockResponse.RESULT][BlockResponse.DATA][BlockResponse.VALUE][BlockResponse.TxResult][
                    BlockResponse.HEIGHT]
                block_height = int(block_height)
                self.scan.process_tx(tx_events, block_height)
            elif msg[BlockResponse.RESULT][BlockResponse.QUERY] == tm_event_NewBlock:
                self.scan.process_block(msg)

    def on_open(self):
        logging.info("connection to fxdex...")
        data = {
            "jsonrpc": "2.0",
            "method": "subscribe",
            "params": [tm_event_NewBlock],
            "id": 1
        }
        data = json.dumps(data).encode()
        self.ws_block.send(data)
        
        data = {
            "jsonrpc": "2.0",
            "method": "subscribe",
            "params": [tm_event_Tx],
            "id": 1
        }
        data = json.dumps(data).encode()
        self.ws_block.send(data)

    def on_close(self):
        logging.info("connection to fxdex websocket is closed")

    def subscribe_block(self):
        websocket.enableTrace(True)
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

class ScanBlock:

    """process block event, then update to sql"""

    def __init__(self):
        self.crud = Crud()

    """
     ************************ process Block ************************
     """
    def process_block(self, message: str):
        try:
            if BlockResponse.DATA not in message[BlockResponse.RESULT]:
                logging.info(f"data not in message: {message}")
                return
            block_height = message[BlockResponse.RESULT][BlockResponse.DATA][BlockResponse.VALUE][
                BlockResponse.BLOCK][BlockResponse.HEADER][BlockResponse.HEIGHT]
            block_height = int(block_height)
            block_time = message[BlockResponse.RESULT][BlockResponse.DATA][BlockResponse.VALUE][
                BlockResponse.BLOCK][BlockResponse.HEADER][BlockResponse.Time]

            timestamp = Timestamp()
            timestamp.FromJsonString(block_time),
            block_datetime = datetime.datetime.utcfromtimestamp(timestamp.ToSeconds())

            block = Block(height=block_height, time=block_datetime)

            sql_block = self.crud.filterone(Block, Block.height == block_height)
            if sql_block is None:
                self.crud.insert(block)
            else:
                self.crud.update(Block, filter=(Block.height == block_height),
                                 updic=block.to_dict())

            begin_block_events = message[BlockResponse.RESULT][BlockResponse.DATA][BlockResponse.VALUE][
                BlockResponse.RESULT_BEGIN_BLOCK][BlockResponse.EVENTS]
            self.process_begin_block(begin_block_events, block_height)

            end_block_events = message[BlockResponse.RESULT][BlockResponse.DATA][BlockResponse.VALUE][
                BlockResponse.RESULT_END_BLOCK][BlockResponse.EVENTS]
            self.process_end_block(end_block_events, block_height)

        except Exception as e:
            logging.error(f"error process block: {traceback.format_exc()}")

    def __update_position(self, position: Position, sql_position: Position):
        # we want to keep only latest position in database
        if position.block_height >= sql_position.block_height:
            self.crud.update(Position, filter=(Position.position_id == position.position_id),
                             updic=position.to_dict())
        elif sql_position.open_height is None or position.block_height < sql_position.open_height:
            self.crud.update(Position, filter=(Position.position_id == position.position_id),
                             updic={'open_height': position.block_height})

    def __update_order(self, order: Order, sql_order: Order):
        # we want to keep only latest order in database
        order.id = sql_order.id
        #if (order.filled_quantity and sql_order.base_quantity) and order.filled_quantity > sql_order.base_quantity:
        #    logging.warning("filled quantity higher than base quantity!")

        if order.block_height >= sql_order.block_height:
            self.crud.update(Order, filter=(Order.order_id == order.order_id),
                             updic=order.to_dict())
        else:
            update_dict = {}
            if order.created_at and not sql_order.created_at:
                update_dict['created_at'] = order.created_at
            if order.open_block_height and not sql_order.open_block_height:
                update_dict['open_block_height'] = order.open_block_height

            self.crud.update(Order, filter=(Order.order_id == order.order_id),
                             updic=update_dict)

    def process_end_block(self, events: str, block_height: int):
        """process fxdex chain EndBlock events"""

        for event in events:
            if event[BlockResponse.TYPE] == EventTypes.New_position:
                position = Position()
                for attribute in event[BlockResponse.Attributes]:
                    key = base64.b64decode(attribute[BlockResponse.Key]).decode('utf8')
                    value = base64.b64decode(attribute[BlockResponse.VALUE]).decode('utf8')

                    # fx.dex.position is proto generate, different from other events
                    value = eval(value)

                    if key == EventKeys.id:
                        position.position_id = int(value)
                    elif key == EventKeys.owner:
                        position.owner = value
                    elif key == EventKeys.pair_id:
                        position.pair_id = value
                    elif key == EventKeys.direction:
                        position.direction = value
                    elif key == EventKeys.entry_price:
                        position.entry_price = Decimal(value)
                    elif key == EventKeys.mark_price:
                        position.mark_price = Decimal(value)
                    elif key == EventKeys.liquidation_price:
                        position.liquidation_price = Decimal(value)
                    elif key == EventKeys.base_quantity:
                        position.base_quantity = Decimal(value)
                    elif key == EventKeys.margin:
                        position.margin = Decimal(value)
                    elif key == EventKeys.leverage:
                        position.leverage = int(value)
                    elif key == EventKeys.unrealized_pnl:
                        position.unrealized_pnl = Decimal(value)
                    elif key == EventKeys.margin_rate:
                        position.margin_rate = Decimal(value)
                    elif key == EventKeys.initial_margin:
                        position.initial_margin = Decimal(value)
                    elif key == EventKeys.pending_order_quantity:
                        position.pending_order_quantity = Decimal(value)

                sql_position = self.crud.filterone(Position, Position.position_id==position.position_id)
                position.status = PositionStatus.Open
                position.block_height = block_height
                position.open_height = block_height

                if sql_position is None:
                    self.crud.insert(position)
                else:
                    self.__update_position(position, sql_position)

            elif event[BlockResponse.TYPE] == EventTypes.Add_position:
                position = self.get_position(event[BlockResponse.Attributes])
                position.status = PositionStatus.Open
                position.block_height = block_height

                sql_position = self.crud.filterone(Position, Position.position_id == position.position_id)
                if sql_position is None:
                    self.crud.insert(position)
                else:
                    self.__update_position(position, sql_position)
                
            elif event[BlockResponse.TYPE] == EventTypes.Full_close_position:
                position = self.get_position(event[BlockResponse.Attributes])
                position.status = PositionStatus.Close
                position.block_height = block_height
                position.close_height = block_height

                sql_position = self.crud.filterone(Position, Position.position_id == position.position_id)
                if sql_position is None:
                    self.crud.insert(position)
                else:
                    self.__update_position(position, sql_position)

            elif event[BlockResponse.TYPE] == EventTypes.Part_close_position:
                position = self.get_position(event[BlockResponse.Attributes])
                position.status = PositionStatus.Open
                position.block_height = block_height

                sql_position = self.crud.filterone(Position, Position.position_id == position.position_id)
                if sql_position is None:
                    self.crud.insert(position)
                else:
                    self.__update_position(position, sql_position)

            elif event[BlockResponse.TYPE] == EventTypes.Cancel_order_expire:
                """update order status to expiration"""
                order = self.get_order(event[BlockResponse.Attributes])
                order.block_height = block_height
                order.cancel_block_height = block_height

                sql_order = self.crud.filterone(Order, Order.order_id == order.order_id)
                if sql_order is None:
                    self.crud.insert(order)
                else:
                    self.__update_order(order, sql_order)

                self.process_orderbook(order, False, block_height)

            elif event[BlockResponse.TYPE] == EventTypes.Order_fill:
                """store order & trade"""
                order = self.get_order(event[BlockResponse.Attributes])
                order.block_height = block_height
                order.filled_block_height = block_height
                sql_order = self.crud.filterone(Order, Order.order_id == order.order_id)

                if sql_order is None:
                    self.crud.insert(order)
                else:
                    self.__update_order(order, sql_order)

                trade = self.get_trade(event[BlockResponse.Attributes])
                trade.block_height = block_height
                self.crud.insert(trade)

                """process orderbook"""
                sql_orderbook = self.crud.get_latest_orderbook_record(trade.deal_price, order.pair_id, order.direction)
                orderbook = Orderbook(price=trade.deal_price, quantity=order.base_quantity,
                                      direction=order.direction, pair_id=order.pair_id,
                                      block_height=block_height)
                if sql_orderbook:
                    orderbook.quantity = sql_orderbook.quantity - trade.matched_quantity
                self.crud.insert(orderbook)

        return

    def process_begin_block(self, events: str, block_height: int):
        """process fxdex chain BeginBlock events"""

        for event in events:
            if event[BlockResponse.TYPE] == EventTypes.Forced_liquidation_position:
                position = self.get_position(event[BlockResponse.Attributes])
                position.status = PositionStatus.Liquidated
                position.block_height = block_height
                position.close_height = block_height

                sql_position = self.crud.filterone(Position, Position.position_id == position.position_id)
                if sql_position is None:
                    self.crud.insert(position)
                else:
                    self.__update_position(position, sql_position)

            elif event[BlockResponse.TYPE] == EventTypes.Liq_cancel_order:
                """liquidation cancel pending close-position order, only update order"""
                order = self.get_order(event[BlockResponse.Attributes])
                order.block_height = block_height
                order.cancel_block_height = block_height

                sql_order = self.crud.filterone(Order, Order.order_id == order.order_id)
                if sql_order is None:
                    self.crud.insert(order)
                else:
                    self.__update_order(order, sql_order)

                self.process_orderbook(order, False, block_height)

            elif event[BlockResponse.TYPE] == EventTypes.Liquidation_position_order:
                """liquidation generate new order, only insert order"""
                order = self.get_order(event[BlockResponse.Attributes])
                order.open_block_height = block_height
                order.block_height = block_height
                order.filled_block_height = block_height

                sql_order = self.crud.filterone(Order, Order.order_id == order.order_id)
                if sql_order is None:
                    self.crud.insert(order)
                self.process_orderbook(order, True, block_height)

            elif event[BlockResponse.TYPE] == EventTypes.Settle_funding:
                """parse settle funding rate log"""
                funding_transfer = FundingTransfer()
                funding_transfer.block_height = block_height
                for attribute in event[BlockResponse.Attributes]:
                    key = base64.b64decode(attribute[BlockResponse.Key]).decode('utf8')
                    value = base64.b64decode(attribute[BlockResponse.VALUE]).decode('utf8')
                    if key == EventKeys.position_id:
                        funding_transfer.position_id = int(value)
                    elif key == EventKeys.owner:
                        funding_transfer.owner = value
                    elif key == EventKeys.pair_id:
                        funding_transfer.pair_id = value
                    elif key == EventKeys.funding_fee:
                        funding_transfer.funding_fee = Decimal(value)

                """in case of duplicate"""
                sql_transfer = self.crud.filterone(FundingTransfer, and_(FundingTransfer.pair_id == funding_transfer.pair_id,
                                                                      FundingTransfer.block_height == funding_transfer.block_height,
                                                                      FundingTransfer.owner == funding_transfer.owner,
                                                                      FundingTransfer.position_id == funding_transfer.position_id,
                                                                      ))
                if sql_transfer is None:
                    self.crud.insert(funding_transfer)
                    """if exist, do not need to update"""
        return

    """
    ************************ process tx ************************
    """
    def process_tx(self, tx_events, block_height):
        """process fxdex chain Transaction events"""
        for event in tx_events:
            if event[BlockResponse.TYPE] == EventTypes.Order or event[
                BlockResponse.TYPE] == EventTypes.Close_position_order:
                """only insert order, if sql order is none, then do not update"""
                order = self.get_order(event[BlockResponse.Attributes])
                order.open_block_height = block_height
                order.block_height = block_height

                sql_order = self.crud.filterone(Order, Order.order_id == order.order_id)
                if sql_order is None:
                    self.crud.insert(order)
                else:
                    self.__update_order(order)  # updates open_block_height, created_at

                self.process_orderbook(order, True, block_height)

            elif event[BlockResponse.TYPE] == EventTypes.Cancel_order:
                """only update order, but in case of not listened create order"""
                order = self.get_order(event[BlockResponse.Attributes])
                order.block_height = block_height
                order.cancel_block_height = block_height
                
                sql_order = self.crud.filterone(Order, Order.order_id == order.order_id)
                if sql_order is None:
                    self.crud.insert(order)
                else:
                    self.__update_order(order, sql_order)

                self.process_orderbook(order, False, block_height)

    """
        add_or_cancel: True means add (append), False means cancel (subtract)
    """

    def process_orderbook(self, order: Order, add_or_cancel: bool, block_height):

        sql_orderbook = self.crud.get_latest_orderbook_record(order.price, order.pair_id, order.direction)

        orderbook = Orderbook(price=order.price, quantity=order.base_quantity,
                              direction=order.direction, pair_id=order.pair_id,
                              block_height=block_height)

        if sql_orderbook:
            if add_or_cancel:
                orderbook.quantity = order.base_quantity + sql_orderbook.quantity
            else:
                orderbook.quantity = sql_orderbook.quantity - order.base_quantity

        self.crud.insert(orderbook)

    def get_position(self, attributes: []) -> Position:
        """decode position data"""
        position = Position()
        for attribute in attributes:
            key = base64.b64decode(attribute[BlockResponse.Key]).decode('utf8')
            value = base64.b64decode(attribute[BlockResponse.VALUE]).decode('utf8')
            if key == EventKeys.position_id:
                position.position_id = int(value)
            elif key == EventKeys.owner:
                position.owner = value
            elif key == EventKeys.pair_id:
                position.pair_id = value
            elif key == EventKeys.direction:
                position.direction = value
            elif key == EventKeys.entry_price:
                position.entry_price = Decimal(value)
            elif key == EventKeys.mark_price:
                position.mark_price = Decimal(value)
            elif key == EventKeys.liquidation_price:
                position.liquidation_price = Decimal(value)
            elif key == EventKeys.base_quantity:
                position.base_quantity = Decimal(value)
            elif key == EventKeys.margin:
                position.margin = Decimal(value)
            elif key == EventKeys.leverage:
                position.leverage = int(value)
            elif key == EventKeys.unrealized_pnl:
                position.unrealized_pnl = Decimal(value)
            elif key == EventKeys.margin_rate:
                position.margin_rate = Decimal(value)
            elif key == EventKeys.initial_margin:
                position.initial_margin = Decimal(value)
            elif key == EventKeys.pending_order_quantity:
                position.pending_order_quantity = Decimal(value)
        return position


    def get_order(self, attributes: []) -> Order:
        """decode order data"""

        order = Order()
        for attribute in attributes:
            key = base64.b64decode(attribute[BlockResponse.Key]).decode('utf8')
            value = base64.b64decode(attribute[BlockResponse.VALUE]).decode('utf8')
            if key == EventKeys.tx_hash:
                order.tx_hash = value
            elif key == EventKeys.order_id:
                order.order_id = value
            elif key == EventKeys.owner:
                order.owner = value
            elif key == EventKeys.pair_id:
                order.pair_id = value
            elif key == EventKeys.direction:
                order.direction = value
            elif key == EventKeys.price:  # to decimal
                order.price = Decimal(value)
            elif key == EventKeys.base_quantity:
                order.base_quantity = Decimal(value)
            elif key == EventKeys.quote_quantity:
                order.quote_quantity = Decimal(value)
            elif key == EventKeys.filled_quantity:
                order.filled_quantity = Decimal(value)
            elif key == EventKeys.filled_avg_price:
                order.filled_avg_price = Decimal(value)
            elif key == EventKeys.remain_locked:
                order.remain_locked = Decimal(value)
            elif key == EventKeys.created_at:
                if value.__contains__('T') and value.__contains__('Z'):
                    timestamp = Timestamp()
                    timestamp.FromJsonString(value),
                    block_datetime = datetime.datetime.utcfromtimestamp(timestamp.ToSeconds())
                    order.created_at = block_datetime
                else:
                    UTC_FORMAT = "%Y-%m-%d %H:%M:%S.%f +0000 UTC"
                    date_value = re.sub('(\d{7,9})', lambda x: x.group()[:6], value)    # microseconds truncated to 6 decimals
                    block_datetime = datetime.datetime.strptime(date_value, UTC_FORMAT)
                    order.created_at = block_datetime
            elif key == EventKeys.leverage:
                order.leverage = int(value)
            elif key == EventKeys.status:
                order.status = value
            elif key == EventKeys.order_type:
                order.order_type = value
            elif key == EventKeys.cost_fee:
                order.cost_fee = Decimal(value)
            elif key == EventKeys.locked_fee:
                order.locked_fee = Decimal(value)
            elif key == EventKeys.cancel_time:  # only cancel order or expire order have cancel_time
                timestamp = Timestamp()
                timestamp.FromJsonString(value),
                block_datetime = datetime.datetime.utcfromtimestamp(timestamp.ToSeconds())
                order.cancel_time = block_datetime

        return order

    def get_trade(self, attributes: []) -> Trade:
        """decode trade data"""

        trade = Trade()
        for attribute in attributes:
            key = base64.b64decode(attribute[BlockResponse.Key]).decode('utf8')
            value = base64.b64decode(attribute[BlockResponse.VALUE]).decode('utf8')
            if key == EventKeys.deal_price:
                trade.deal_price = Decimal(value)
            elif key == EventKeys.matched_quantity:
                trade.matched_quantity = Decimal(value)
            elif key == EventKeys.order_id:
                trade.order_id = value
            elif key == EventKeys.owner:
                trade.owner = value
            elif key == EventKeys.pair_id:
                trade.pair_id = value
            elif key == EventKeys.direction:
                trade.direction = value
            elif key == EventKeys.price:  # to decimal
                trade.price = Decimal(value)
            elif key == EventKeys.base_quantity:
                trade.base_quantity = Decimal(value)
            elif key == EventKeys.quote_quantity:
                trade.quote_quantity = Decimal(value)
            elif key == EventKeys.filled_quantity:
                trade.filled_quantity = Decimal(value)
            elif key == EventKeys.filled_avg_price:
                trade.filled_avg_price = Decimal(value)
            elif key == EventKeys.order_type:
                trade.order_type = value
            elif key == EventKeys.cost_fee:
                trade.cost_fee = Decimal(value)
        return trade