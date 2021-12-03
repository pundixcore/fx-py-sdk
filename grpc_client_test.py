import unittest

import grpc

import grpc_client


class MyTestCase(unittest.TestCase):
    def test_grpc(self):
        channel = grpc.insecure_channel('44.196.199.119:9090')

        mnemonic_list = "crime indicate code innocent brush loud among labor girl print solar flower visit ridge garage scan visual finger gaze rack toy road mimic divorce"

        balances = grpc_client.query_all_balances(channel=channel, address="dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy")
        print(balances)

        account = grpc_client.query_account_info(channel=channel, address="dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy")
        print(account)

if __name__ == '__main__':
    unittest.main()
