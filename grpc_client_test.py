import unittest

import grpc

import grpc_client


class MyTestCase(unittest.TestCase):
    def test_grpc(self):
        channel = grpc.insecure_channel('localhost:9090')

        balances = grpc_client.query_all_balances(channel=channel, address="fx1sw0m27f2hn0mmmzw89dhr3xpmyy2q6rsvpugkh")
        print(balances)

        account = grpc_client.query_account_info(channel=channel, address="fx1sw0m27f2hn0mmmzw89dhr3xpmyy2q6rsvpugkh")
        print(account)


if __name__ == '__main__':
    unittest.main()
