import base64

import websocket
import json
import logging
import os
from fx_py_sdk import constants
import threading
from fx_py_sdk.model.block import *
from fx_py_sdk.model.model import *
from fx_py_sdk.model.crud import *
from decimal import Decimal

reconnect_block_count = 0
reconnect_tx_count = 0

class DexScan:
    def __init__(self):
        self.crud = Crud()
        self.wss_url = ''
        network_url = os.environ[constants.EnvVar.NETWORK]
        if network_url == constants.NetworkENV.LOCAL:
            self.wss_url = constants.Network.LOCAL
        elif network_url == constants.NetworkENV.DEVNET:
            self.wss_url = constants.Network.DEVNET
        elif network_url == constants.NetworkENV.TESTNET:
            self.wss_url = constants.Network.TESTNET
        elif network_url == constants.NetworkENV.MAINNET:
            self.wss_url = constants.Network.MAINNET

        self.ws_block = None
        self.ws_tx = None
        threading.Thread(
            target=self.subscribe_block()
        ).start()
        threading.Thread(
            target=self.subscribe_tx()
        ).start()

    def _get_ws_endpoint_url(self):
        return f"{self.wss_url}websocket"

    """
    ************************ subscribe Block ************************
    """
    def on_error(self, error):
        global reconnect_block_count
        print("websocket caught: ", error)
        if type(error) == ConnectionRefusedError or \
                type(error) == ConnectionResetError or \
                type(error) == websocket._exceptions.WebSocketConnectionClosedException:
            print("正在尝试第 %d 次重连" % reconnect_block_count)
            reconnect_block_count += 1
            if reconnect_block_count < 10:
                self.subscribe_block()
        else:
            print("error: ", error)

    def on_message(self, message):
        global reconnect_block_count
        reconnect_block_count = 0
        self._process_block(json.loads(message))

    def on_open(self):
        logging.info("connection to fxdex...")
        data = {
            "jsonrpc": "2.0",
            "method": "subscribe",
            "params": ["tm.event='NewBlock'"],
            "id": 1
        }
        data = json.dumps(data).encode()
        self.ws_block.send(data)

    def on_close(self):
        logging.info("connection to fxdex websocket is closed")

    def subscribe_block(self):
        websocket.enableTrace(True)
        print(self._get_ws_endpoint_url())
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

    def _process_block(self, message: str):
        try:
            if BlockResponse.DATA not in message[BlockResponse.RESULT]:
                logging.info(f"data not in message yet {message}")
                return
            block_number = message[BlockResponse.RESULT][BlockResponse.DATA][BlockResponse.VALUE][
                BlockResponse.BLOCK][BlockResponse.HEADER][BlockResponse.HEIGHT]
            block_number = int(block_number)

            begin_block_events = message[BlockResponse.RESULT][BlockResponse.DATA][BlockResponse.VALUE][
                BlockResponse.RESULT_BEGIN_BLOCK][BlockResponse.EVENTS]
            self._process_begin_block(begin_block_events, block_number)

            end_block_events = message[BlockResponse.RESULT][BlockResponse.DATA][BlockResponse.VALUE][
                BlockResponse.RESULT_END_BLOCK][BlockResponse.EVENTS]
            self._process_end_block(end_block_events, block_number)

        except Exception as e:
            logging.error("error process block: ", e)

    def _process_end_block(self, events: str, block_number: int):
        for event in events:
            if event[BlockResponse.TYPE] == EventTypes.Add_position:
                position = Position()
                for attribute in event[BlockResponse.Attributes]:
                    key = base64.b64decode(attribute[BlockResponse.Key]).decode('utf8')
                    value = base64.b64decode(attribute[BlockResponse.VALUE]).decode('utf8')
                    if key == EventKeys.position_id:
                        try:
                            position = self.crud.filterone(Position, Position.position_id == value)
                        except Exception as e:
                            logging.error("error filter position: ", e)
                    elif key == EventKeys.pair_id:
                        position.pair_id = value
                    elif key == EventKeys.margin:
                        position.margin = Decimal(value)
                    elif key == EventKeys.mark_price:
                        position.mark_price = Decimal(value)
                    elif key == EventKeys.base_quantity:
                        position.base_quantity = Decimal(value)
                    elif key == EventKeys.direction:
                        position.direction = value
                    elif key == EventKeys.owner:
                        position.owner = value
                    elif key == EventKeys.leverage:
                        position.leverage = int(value)
                    elif key == EventKeys.entry_price:
                        position.entry_price = Decimal(value)
                    elif key == EventKeys.liquidation_price:
                        position.liquidation_price = Decimal(value)
                    elif key == EventKeys.margin_rate:
                        position.margin_rate = Decimal(value)
                    elif key == EventKeys.deal_price:
                        position.deal_price = Decimal(value)
                try:
                    self.crud.update(Position, filter=(Position.position_id == position.position_id),
                                     updic=position.to_dict())
                except Exception as e:
                    logging.error("update position error: ", e)

            elif event[BlockResponse.TYPE] == EventTypes.Order_fill:
                for attribute in event[BlockResponse.Attributes]:
                    key = base64.b64decode(attribute[BlockResponse.Key]).decode('utf8')
                    value = base64.b64decode(attribute[BlockResponse.VALUE]).decode('utf8')

            elif event[BlockResponse.TYPE] == EventTypes.New_position:
                position = Position()
                for attribute in event[BlockResponse.Attributes]:
                    key = base64.b64decode(attribute[BlockResponse.Key]).decode('utf8')
                    value = base64.b64decode(attribute[BlockResponse.VALUE]).decode('utf8')

                    # fx.dex.position is proto generate, different from other events
                    value = eval(value)

                    if key == EventKeys.id:
                        position.position_id = value
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
                try:
                    self.crud.insert(position)
                except Exception as e:
                    logging.error("insert position error: ", e)

            elif event[BlockResponse.TYPE] == EventTypes.Cancel_order_expire:
                for attribute in event[BlockResponse.Attributes]:
                    key = base64.b64decode(attribute[BlockResponse.Key]).decode('utf8')
                    value = base64.b64decode(attribute[BlockResponse.VALUE]).decode('utf8')

            elif event[BlockResponse.TYPE] == EventTypes.Part_close_position:
                for attribute in event[BlockResponse.Attributes]:
                    key = base64.b64decode(attribute[BlockResponse.Key]).decode('utf8')
                    value = base64.b64decode(attribute[BlockResponse.VALUE]).decode('utf8')

            elif event[BlockResponse.TYPE] == EventTypes.Full_close_position:
                for attribute in event[BlockResponse.Attributes]:
                    key = base64.b64decode(attribute[BlockResponse.Key]).decode('utf8')
                    value = base64.b64decode(attribute[BlockResponse.VALUE]).decode('utf8')
                    print(key, value)
        return

    def _process_begin_block(self, events: str, block_number: int):
        for event in events:
            if event[BlockResponse.TYPE] == EventTypes.Forced_liquidation_position:
                print(event)
            elif event[BlockResponse.TYPE] == EventTypes.Liq_cancel_order:
                print(event)
            elif event[BlockResponse.TYPE] == EventTypes.Liquidation_position_order:
                print(event)
        return

    """
    ************************ subscribe tx ************************
    """
    def on_error_tx(self, error):
        global reconnect_tx_count
        print("tx websocket caught: ", error)
        if type(error) == ConnectionRefusedError or \
                type(error) == ConnectionResetError or \
                type(error) == websocket._exceptions.WebSocketConnectionClosedException:
            print("正在尝试第%d次重连" % reconnect_tx_count)
            reconnect_tx_count += 1
            if reconnect_tx_count < 10:
                self.subscribe_tx()
        else:
            print("tx websocket error: ", error)

    def on_message_tx(self, message):
        global reconnect_tx_count
        reconnect_tx_count = 0
        self._process_tx(json.loads(message))

    def on_open_tx(self):
        logging.info("connection to fxdex...")
        data = {
            "jsonrpc": "2.0",
            "method": "subscribe",
            "params": ["tm.event='Tx'"],
            "id": 1
        }
        data = json.dumps(data).encode()
        self.ws_tx.send(data)

    def subscribe_tx(self):
        websocket.enableTrace(True)
        self.ws_tx = websocket.WebSocketApp(self._get_ws_endpoint_url(),
                                    on_message=self.on_message_tx,
                                    on_error=self.on_error_tx,
                                    on_close=self.on_close,
                                    on_open=self.on_open_tx)
        try:
            self.ws_tx.run_forever()
        except KeyboardInterrupt:
            self.ws_tx.close()
        except:
            self.ws_tx.close()

    def _process_tx(self, message: str):
        try:
            if BlockResponse.RESULT not in message:
                logging.info(f"result not in message yet {message}")
                return
            if BlockResponse.DATA not in message[BlockResponse.RESULT]:
                logging.info(f"data not in message yet {message}")
                return
            if BlockResponse.VALUE not in message[BlockResponse.RESULT][BlockResponse.DATA]:
                logging.info(f"value not in message yet {message}")
                return
            if BlockResponse.TxResult not in message[BlockResponse.RESULT][BlockResponse.DATA][BlockResponse.VALUE]:
                logging.info(f"tx_result not in message yet {message}")
                return
            tx_events = message[BlockResponse.RESULT][BlockResponse.DATA][BlockResponse.VALUE][BlockResponse.TxResult][BlockResponse.RESULT][BlockResponse.EVENTS]
            for event in tx_events:
                if event[BlockResponse.TYPE] == EventTypes.Order or event[BlockResponse.TYPE] == EventTypes.Close_position_order:
                    order = Order()
                    block_number = message[BlockResponse.RESULT][BlockResponse.DATA][BlockResponse.VALUE][BlockResponse.TxResult][BlockResponse.HEIGHT]
                    order.block_number = int(block_number)
                    for attribute in event[BlockResponse.Attributes]:
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
                        elif key == EventKeys.price: #to decimal
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
                            order.created_at = value
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
                    try:
                        self.crud.insert(order)
                    except Exception as e:
                        logging.error("insert order error: ", e)

                elif event[BlockResponse.TYPE] == EventTypes.Cancel_order:
                    cancel_order = Order()
                    for attribute in event[BlockResponse.Attributes]:
                        key = base64.b64decode(attribute[BlockResponse.Key]).decode('utf8')
                        value = base64.b64decode(attribute[BlockResponse.VALUE]).decode('utf8')
                        if key == EventKeys.order_id:
                            cancel_order = self.crud.filterone(Order, Order.order_id==value)
                            print(cancel_order.to_dict)
                        elif key == EventKeys.base_quantity:
                            cancel_order.base_quantity = Decimal(value)
                        elif key == EventKeys.quote_quantity:
                            cancel_order.quote_quantity = Decimal(value)
                        elif key == EventKeys.filled_quantity:
                            cancel_order.filled_quantity = Decimal(value)
                        elif key == EventKeys.filled_avg_price:
                            cancel_order.filled_avg_price = Decimal(value)
                        elif key == EventKeys.status:
                            cancel_order.status = value
                        elif key == EventKeys.cost_fee:
                            cancel_order.cost_fee = Decimal(value)
                        elif key == EventKeys.locked_fee:
                            cancel_order.locked_fee = Decimal(value)
                    try:
                        self.crud.update(Order, filter=(Order.order_id == cancel_order.order_id), updic=cancel_order.to_dict())
                    except Exception as e:
                        logging.error("update order error: ", e)

        except Exception as e:
            logging.error("error process tx: ", e)


"""
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32000,
    "message": "Server error",
    "data": "subscription was cancelled (reason: client is not pulling messages fast enough)"
  }
}
"""
