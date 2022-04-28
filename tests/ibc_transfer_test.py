import unittest
from fx_py_sdk.ibc_transfer import ConfigsKeys,Ibc_transfer
from fx_py_sdk.grpc_client import GRPCClient

class MyTestCase(unittest.TestCase):
    def test_query_balances(self):
        ibc = Ibc_transfer()
        print(ibc.cfg[ConfigsKeys.IBC_CHANNELS][ConfigsKeys.BTC_FXCore])

    def test_transfer_to_one_chain(self):
        ibc = Ibc_transfer()
        mnemonic = "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt"

        ibc.transfer_to_one_chain(mnemonic, "USDT", "0xA1FD17f3624B64cE5Cd0d6Ed22298340488507d3", ConfigsKeys.SPY)

