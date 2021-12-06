import unittest
import wallet
import grpc
import grpc_client
import bech32
from grpc_client import GRPCClient


class MyTestCase(unittest.TestCase):
    def test_grpc_query(self):
        client = GRPCClient('localhost:9090')

        balances = client.query_all_balances(address="fx1yt8navfnvwe9k7qcp96fueamj8u5z8hz2y4th7")
        print(balances)

        account = client.query_account_info(address="fx1yt8navfnvwe9k7qcp96fueamj8u5z8hz2y4th7")

        print(account)

        hrp, data = bech32.bech32_decode('dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy')
        converted = bech32.convertbits(data, 5, 8, False)
        print(bytes(converted))
        positions = grpc_client.query_all_positions(channel=channel, owner=bytes(converted), pair_id="tsla:usdt")
        print(positions)

if __name__ == '__main__':
    unittest.main()
