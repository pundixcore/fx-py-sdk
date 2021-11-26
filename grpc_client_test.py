import unittest

from grpc_client import GRPCClient


class MyTestCase(unittest.TestCase):
    def test_grpc_query(self):
        client = GRPCClient('localhost:9090')

        balances = client.query_all_balances(address="fx1yt8navfnvwe9k7qcp96fueamj8u5z8hz2y4th7")
        print(balances)

        account = client.query_account_info(address="fx1yt8navfnvwe9k7qcp96fueamj8u5z8hz2y4th7")
        print(account)


if __name__ == '__main__':
    unittest.main()
