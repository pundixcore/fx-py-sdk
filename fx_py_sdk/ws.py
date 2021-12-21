import websocket
import json
import logging
import os
from fx_py_sdk import constants
import threading
from fx_py_sdk.model.block import *

class DexScan:

    def __init__(self):
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
        threading.Thread(
            target=self.subscribe_block
        ).start()
        threading.Thread(
            target=self.subscribe_tx
        ).start()

    def _get_ws_endpoint_url(self):
        return f"{self.wss_url}websocket"

    def subscribe_block(self):

        ws = None

        def on_error(ws, error):
            reconnect_count = 0
            print("websocket caught: ", error)
            if type(error) == ConnectionRefusedError or \
                    type(error) == ConnectionResetError or \
                    type(error) == websocket._exceptions.WebSocketConnectionClosedException:
                print("正在尝试第%d次重连" % reconnect_count)
                reconnect_count += 1
                if reconnect_count < 10:
                    connection(ws)
            else:
                print("其他error!")

        def on_message(ws, message):
            self._process_block(json.loads(message))

        def on_open(ws):
            logging.info("connection to fxdex...")
            data = {
                "jsonrpc": "2.0",
                "method": "subscribe",
                "params": ["tm.event='NewBlock'"],
                "id": 1
            }
            self.__send_message(ws, data)

        def on_close(ws):
            logging.info("connection to fxdex websocket is closed")

        def connection(ws):
            websocket.enableTrace(True)
            print(self._get_ws_endpoint_url())
            ws = websocket.WebSocketApp(self._get_ws_endpoint_url(),
                                        on_message=on_message,
                                        on_error=on_error,
                                        on_close=on_close)
            ws.on_open = on_open
            try:
                ws.run_forever()
            except KeyboardInterrupt:
                ws.close()
            except:
                ws.close()

        connection(ws)


    def subscribe_tx(self):

        ws = None

        def on_error(ws, error):
            reconnect_count = 0
            print("websocket caught: ", error)
            if type(error) == ConnectionRefusedError or \
                    type(error) == ConnectionResetError or \
                    type(error) == websocket._exceptions.WebSocketConnectionClosedException:
                print("正在尝试第%d次重连" % reconnect_count)
                reconnect_count += 1
                if reconnect_count < 10:
                    connection(ws)
            else:
                print("其他error!")

        def on_message(ws, message):
            self._process_tx(json.loads(message))

        def on_open(ws):
            logging.info("connection to fxdex...")
            data = {
                "jsonrpc": "2.0",
                "method": "subscribe",
                "params": ["tm.event='Tx'"],
                "id": 1
            }
            self.__send_message(ws, data)

        def on_close(ws):
            logging.info("connection to fxdex websocket is closed")

        def connection(ws):
            websocket.enableTrace(True)
            print(self._get_ws_endpoint_url())
            ws = websocket.WebSocketApp(self._get_ws_endpoint_url(),
                                        on_message=on_message,
                                        on_error=on_error,
                                        on_close=on_close)
            ws.on_open = on_open
            try:
                ws.run_forever()
            except KeyboardInterrupt:
                ws.close()
            except:
                ws.close()

        connection(ws)

    def __send_message(self, ws, message_dict):
        data = json.dumps(message_dict).encode()
        ws.send(data)

    def _process_block(self, message: str):
        try:
            if BlockResponse.DATA not in message[BlockResponse.RESULT]:
                logging.info(f"data not in message yet {message}")
                return
            begin_block_events = message[BlockResponse.RESULT][BlockResponse.DATA][BlockResponse.VALUE][BlockResponse.RESULT_BEGIN_BLOCK][BlockResponse.EVENTS]
            self._process_begin_block(begin_block_events)

            end_block_events = message[BlockResponse.RESULT][BlockResponse.DATA][BlockResponse.VALUE][BlockResponse.RESULT_END_BLOCK][BlockResponse.EVENTS]
            self._process_end_block(end_block_events)

        except Exception as e:
            logging.error("error process block: ", e)

    def _process_end_block(self, events: str):
        for event in events:
            if event[BlockResponse.TYPE] == EventTypes.Add_position:
                print(event)
            elif event[BlockResponse.TYPE] == EventTypes.Order_fill:
                print(event)
            elif event[BlockResponse.TYPE] == EventTypes.New_position:
                print(event)
            elif event[BlockResponse.TYPE] == EventTypes.Cancel_order_expire:
                print(event)
            elif event[BlockResponse.TYPE] == EventTypes.Part_close_position:
                print(event)
            elif event[BlockResponse.TYPE] == EventTypes.Full_close_position:
                print(event)

        return

    def _process_begin_block(self, events: str):
        for event in events:
            if event[BlockResponse.TYPE] == EventTypes.Forced_liquidation_position:
                print(event)
            elif event[BlockResponse.TYPE] == EventTypes.Liq_cancel_order:
                print(event)
            elif event[BlockResponse.TYPE] == EventTypes.Liquidation_position_order:
                print(event)

        return

    def _process_tx(self, message: str):
        try:
            if BlockResponse.DATA not in message[BlockResponse.RESULT]:
                logging.info(f"data not in message yet {message}")
                return
            tx_events = message[BlockResponse.RESULT][BlockResponse.DATA][BlockResponse.VALUE][BlockResponse.TxResult][BlockResponse.RESULT][BlockResponse.EVENTS]
            for event in tx_events:
                if event[BlockResponse.TYPE] == EventTypes.Order:
                    print(event)
                elif event[BlockResponse.TYPE] == EventTypes.Cancel_order:
                    print(event)
                elif event[BlockResponse.TYPE] == EventTypes.Close_position_order:
                    print(event)

        except Exception as e:
            logging.error("error process tx: ", e)




