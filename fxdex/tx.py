import asyncio
import datetime
import logging
import time
import uuid as u

from cosmos.bank.v1beta1.query_pb2 import QueryBalanceRequest
from fx.dex.query_pb2 import *
from fx.dex.tx_pb2 import MsgCreateOrder, MsgClosePosition, MsgCancelOrder
from fxdex.sdk.fxdex import Fxdex

def create_order(sdk, pair_id):
    sdk.dex.with_transactions(
        [
            MsgCreateOrder(
                owner=sdk.wallet.address,
                pair_id=pair_id,
                key="firstKey",
                value="firstValue".encode("utf-8"),
                lease=Lease(hours=1),
            ),
        ],
        memo="optionalMemo",
    )



if __name__ == "__main__":
    sdk = Fxdex(
        mnemonic="space dilemma domain payment snap crouch arrange"
        " fantasy draft shaft fitness rain habit dynamic tip "
        "faith mushroom please power kick impulse logic wet cricket",
        host="wss://127.0.0.1",
        port=26657,
        max_gas=100000000,
        gas_price=0.00000006,
        logging_level=logging.DEBUG,
    )

