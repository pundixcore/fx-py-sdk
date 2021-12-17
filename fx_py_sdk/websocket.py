import asyncio
import ujson as json
import logging
from random import random
from typing import Dict, Callable, Awaitable, Optional, List

import websockets as ws

class ReconnectingWebsocket:

    MAX_RECONNECTS: int = 5
    MAX_RECONNECT_SECONDS: int = 60
    MIN_RECONNECT_WAIT = 0.1
    TIMEOUT: int = 10
    PROTOCOL_VERSION: str = '1.0.0'

    def __init__(self, loop, coro):
        self._loop = loop
        self._log = logging.getLogger(__name__)
        self._coro = coro
        self._reconnect_attempts: int = 0
        self._conn = None
        self._connect_id: int = None
        self._ping_timeout = 60
        self._socket: Optional[ws.client.WebSocketClientProtocol] = None
        self.wss_url = "ws://44.196.199.119:26657"
        self._connect()

    def _connect(self):
        self._conn = asyncio.ensure_future(self._run())

    def _get_ws_endpoint_url(self):
        return f"{self.wss_url}ws"

    async def _run(self):

        keep_waiting: bool = True

        logging.info(f"connecting to {self._get_ws_endpoint_url()}")
        try:
            async with ws.connect(self._get_ws_endpoint_url(), loop=self._loop) as socket:
                self._on_connect(socket)

                try:
                    while keep_waiting:
                        try:
                            evt = await asyncio.wait_for(self._socket.recv(), timeout=self._ping_timeout)
                        except asyncio.TimeoutError:
                            self._log.error("no message in {} seconds".format(self._ping_timeout))
                            await self.send_keepalive()
                        except asyncio.CancelledError:
                            self._log.error("cancelled error")
                            await self.ping()
                        else:
                            try:
                                evt_obj = json.loads(evt)
                            except ValueError:
                                pass
                            else:
                                await self._coro(evt_obj)
                except ws.ConnectionClosed as e:
                    self._log.error('conn closed:{}'.format(e))
                    keep_waiting = False
                    await self._reconnect()
                except Exception as e:
                    self._log.error('ws exception:{}'.format(e))
                    keep_waiting = False
                    await self._reconnect()
        except Exception as e:
            logging.info(f"websocket error: {e}")

    def _on_connect(self, socket):
        self._socket = socket
        self._reconnect_attempts = 0

    async def _reconnect(self):
        await self.cancel()
        self._reconnect_attempts += 1
        if self._reconnect_attempts < self.MAX_RECONNECTS:

            self._log.debug(f"websocket reconnecting {self.MAX_RECONNECTS - self._reconnect_attempts} attempts left")
            reconnect_wait = self._get_reconnect_wait(self._reconnect_attempts)
            self._log.debug(f' waiting {reconnect_wait}')
            await asyncio.sleep(reconnect_wait)
            self._connect()
        else:
            # maybe raise an exception
            self._log.error(f"websocket could not reconnect after {self._reconnect_attempts} attempts")
            pass

    def _get_reconnect_wait(self, attempts: int) -> int:
        expo = 2 ** attempts
        return round(random() * min(self.MAX_RECONNECT_SECONDS, expo - 1) + 1)

    async def send_keepalive(self):
        msg = {"method": "keepAlive"}
        await self._socket.send(json.dumps(msg, ensure_ascii=False))

    async def send_message(self, msg, retry_count=0):
        if not self._socket:
            if retry_count < 5:
                await asyncio.sleep(1)
                await self.send_message(msg, retry_count + 1)
            else:
                logging.info("Unable to send, not connected")
        else:
            await self._socket.send(json.dumps(msg, ensure_ascii=False))

    async def ping(self):
        await self._socket.ping()

    async def cancel(self):
        try:
            self._conn.cancel()
        except asyncio.CancelledError:
            pass
