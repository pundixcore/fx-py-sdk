#!/usr/bin/env python
# coding='uft8'

import sys
import os
import asyncio
from fx_py_sdk import scan
import logging

rootPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(rootPath)

async def main():
    logging.basicConfig(level=logging.DEBUG)
    rpc_scan = scan.RpcScan()
    rpc_scan.process_block()

    # scan.WebsocketScan()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
