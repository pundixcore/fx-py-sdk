import asyncio
import itertools
from typing import Callable, Awaitable, Optional, Dict

from fx_py_sdk.websocket import ReconnectingWebsocket
from fx_py_sdk.rpc.request import RpcRequest
import logging


class ReconnectingRpcWebsocket(ReconnectingWebsocket):

    id_generator = itertools.count(1)

    def _get_ws_endpoint_url(self):
        return f"{self.wss_url}/websocket"

    async def send_keepalive(self):
        await self.send_rpc_message('keepAlive')

    async def send_rpc_message(self, method, params=None, retry_count=0):
        if not self._socket:
            if retry_count < 5:
                await asyncio.sleep(1)
                await self.send_rpc_message(method, params, retry_count + 1)
        else:
            req = RpcRequest(method, next(self.id_generator), params)
            await self._socket.send(str(req))

    async def ping(self):
        await self.send_rpc_message('ping')

    async def cancel(self):
        try:
            self._conn.cancel()
        except asyncio.CancelledError:
            pass

class WebsocketRpcClient():
    def __init__(self):

        self._callback: Callable[[int], Awaitable[str]]
        self._conn = None
        self._loop = None
        self._log = logging.getLogger(__name__)

    async def _recv(self, msg: Dict):
        await self._callback(msg)

    @classmethod
    async def create(cls, loop, callback: Callable[[int], Awaitable[str]]):
        """
        :param loop: asyncio loop
        :param callback: async callback function to receive messages
        :return:
        """
        self = WebsocketRpcClient()
        self._loop = loop
        self._callback = callback
        self._conn = ReconnectingRpcWebsocket(loop, self._recv)
        return self

    async def subscribe(self, query):
        """Subscribe for events via WebSocket.
        """
        req_msg = {
            "query": query
        }
        await self._conn.send_rpc_message('subscribe', req_msg)

    async def unsubscribe(self, query):
        """Unsubscribe from events via WebSocket.
        """
        req_msg = {
            "query": query
        }
        await self._conn.send_rpc_message('unsubscribe', req_msg)

    async def unsubscribe_all(self):
        """Unsubscribe from events via WebSocket.
        """
        await self._conn.send_rpc_message('unsubscribe_all')

