#!/usr/bin/env python
# coding='uft8'

from fx_py_sdk.fx_rpc.rpc import HttpRpcClient
from fx_py_sdk.model.model import Sql
import asyncio
from fx_py_sdk import constants, scan
import logging
import os
import time

async def main():
    """rpc and websocket should run on the same time"""
    rpc_page_size = int(os.environ.get('RPC_PAGE_SIZE', '10'))
    rpc_max_retries = int(os.environ.get('RPC_MAX_RETRIES', '10'))

    logging.info(f'Running {rpc_page_size} threads for RPC calls')
    scan.ScanManager(rpc_page_size=rpc_page_size,
                     rpc_max_retries=rpc_max_retries)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info('Waiting for database to initialize...')

    time.sleep(10)      # give some time for db to initialize

    # Initialize database
    sql = Sql(database="fxdex")

    sql.create_table()  # creates tables only if not created
    sql.initialize_wallets()
    sql.initialize_error_log_height(
        starting_height=os.environ.get('INITIAL_ERROR_LOG_HEIGHT')
    )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
