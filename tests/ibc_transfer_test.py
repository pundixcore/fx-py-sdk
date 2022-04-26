import unittest
from fx_py_sdk.ibc_transfer import ConfigsKeys,Ibc_transfer
from fx_py_sdk.grpc_client import GRPCClient

class MyTestCase(unittest.TestCase):
    def test_query_balances(self):
        ibc = Ibc_transfer()
        print(ibc.cfg[ConfigsKeys.IBC_CHANNELS][ConfigsKeys.BTC_FXCore])

    def test_transfer_to_one_chain(self):
        ibc = Ibc_transfer()
        mnemonic = "tilt lumber reopen beach logic view purse note unfair harsh already sense affair worry magic century dress captain anger sniff range whip helmet boy"
        ibc.transfer_to_one_chain(mnemonic, "USDT", "0xA1FD17f3624B64cE5Cd0d6Ed22298340488507d3", ConfigsKeys.SPY)

