import unittest
import wallet
import grpc
import grpc_client
import bech32
from grpc_client import GRPCClient
from builder import TxBuilder


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

        tx_builder = TxBuilder(priv_key, chain_id, account.account_number)

        tx_response = cli.create_order(tx_builder, 'tsla:usdt', 'BUY', '100000000000000000',
                                       '100000000000000000000000000000000', 10)
        print(tx_response)


if __name__ == '__main__':
    unittest.main()
