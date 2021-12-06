import unittest
import wallet
import grpc
import grpc_client
import bech32
from grpc_client import GRPCClient


class MyTestCase(unittest.TestCase):
    def test_grpc_query(self):
        client = GRPCClient('44.196.199.119:9090')

        # balances = client.query_all_balances(address="fx1yt8navfnvwe9k7qcp96fueamj8u5z8hz2y4th7")
        # print(balances)
        #
        # account = client.query_account_info(address="fx1yt8navfnvwe9k7qcp96fueamj8u5z8hz2y4th7")
        # print(account)


        positions = client.query_positions(owner='dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy', pair_id="tsla:usdt")
        print(positions)

if __name__ == '__main__':
    unittest.main()
