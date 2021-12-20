import asyncio
import logging
from fx_py_sdk.rpc.websockets import WebsocketRpcClient
from fx_py_sdk.model.block import BlockResponse, BlockResponseValue, OrderFilledFields
import json

class DexExploer:
    def _event_orders_filled(self, message: str):
        try:
            if BlockResponse.DATA not in message[BlockResponse.RESULT]:
                logging.info(f"data not in message yet {message}")
                return
            data = message[BlockResponse.RESULT][BlockResponse.DATA]
            if self._is_any_order_filled(data):
                events = message[BlockResponse.RESULT][BlockResponse.EVENTS]
                filled_events = self._pack_order_filled_events(events)
                if self.recording:
                    self.recorded_orders = self.recorded_orders + filled_events
                logging.info(f"filled_events {filled_events}")
        except Exception as e:
            logging.error("error checking orders filled", e)

    async def handle_msg(self, msg):
        # self._event_orders_filled(json.loads(msg))
        print(json.dumps(msg))

    async def explorer(self):
        wrc = await WebsocketRpcClient.create(None, self.handle_msg)
        await wrc.subscribe("tm.event = 'NewBlock'")






