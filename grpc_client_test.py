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

        print(positions['positions'])

        a = "c\304\347\'1C\224\2206\355\231\237|pwR\004\"\234G"
        print(a)

    def test_create_order(self):
        priv_key = wallet.seed_to_privkey(
            "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt")

        address = priv_key.to_address()
        print('address:', address)

        cli = GRPCClient('44.196.199.119:9090')
        chain_id = cli.query_chain_id()
        print('chain_id:', chain_id)

        account = cli.query_account_info(address)
        print('account, number:', account.account_number, 'sequence:', account.sequence)

        hrp, data = bech32.bech32_decode(address)
        converted = bech32.convertbits(data, 5, 8, False)

        cli.create_order(priv_key, account.account_number, account.sequence, chain_id,
                         bytes(converted), "tsla:usdt", 'BUY', b"100000000000000000".decode('utf-8'), b"100000000000000000000000000000000".decode('utf-8'), 10)

if __name__ == '__main__':
    unittest.main()
