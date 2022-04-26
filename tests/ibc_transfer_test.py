import base64
import hashlib
import unittest

from eth_account import Account

from fx_py_sdk import wallet
from fx_py_sdk.ibc_transfer import ConfigsKeys,Ibc_transfer
from fx_py_sdk.grpc_client import GRPCClient, DEFAULT_GRPC_NONE, DEFAULT_DEC
from fx_py_sdk.builder import TxBuilder
from fx_py_sdk.codec.cosmos.base.v1beta1.coin_pb2 import Coin
from fx_py_sdk.codec.fx.dex.v1.order_pb2 import *
import decimal
from fx_py_sdk.codec.cosmos.tx.v1beta1.service_pb2 import BROADCAST_MODE_BLOCK, BROADCAST_MODE_SYNC
from google.protobuf.json_format import MessageToJson
import json
from google.protobuf.timestamp_pb2 import Timestamp


class MyTestCase(unittest.TestCase):
    def test_query_balances(self):
        client = Ibc_transfer()
        print(client.cfg[ConfigsKeys.IBC_CHANNELS][ConfigsKeys.BTC_FXCore])

