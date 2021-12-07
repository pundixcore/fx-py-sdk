import unittest
import wallet
import grpc
import grpc_client
import bech32
from grpc_client import GRPCClient
from builder import TxBuilder
from cosmos.base.v1beta1.coin_pb2 import Coin


class MyTestCase(unittest.TestCase):

    def test_query_balances(self):
        client = GRPCClient('44.196.199.119:9090')
        balances = client.query_all_balances(address="dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy")
        print(balances)

    def test_query_balance(self):
        client = GRPCClient('44.196.199.119:9090')
        balances = client.query_balance(address="dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy", denom="FX")
        print(balances)

    def test_query_gas_price(self):
        client = GRPCClient('44.196.199.119:9090')
        res = client.query_gas_price()
        print(res)

    def test_query_account(self):
        client = GRPCClient('44.196.199.119:9090')
        account = client.query_account_info(address="dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy")
        print(account)

    def test_query_positions(self):
        client = GRPCClient('44.196.199.119:9090')
        resp = client.query_positions(owner='dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy', pair_id="tsla:usdt")
        print(resp)
        owner = resp.positions.positions[0].owner
        print(owner)

    def test_query_order(self):
        client = GRPCClient('44.196.199.119:9090')
        resp = client.query_order(order_id='ID-880797-1')
        print(resp)

    def test_query_orders(self):
        client = GRPCClient('44.196.199.119:9090')
        resp = client.query_orders(order_id='ID-880797-1')
        print(resp)

    def test_create_order(self):
        cli = GRPCClient('44.196.199.119:9090')

        priv_key = wallet.seed_to_privkey(
            "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt")

        address = priv_key.to_address()
        print('address:', address)

        chain_id = cli.query_chain_id()
        print('chain_id:', chain_id)

        account = cli.query_account_info(address)
        print('account number:', account.account_number, 'sequence:', account.sequence)

        tx_builder = TxBuilder(priv_key, chain_id, account.account_number, Coin(amount='60000000', denom='FX'))

        tx_response = cli.create_order(tx_builder, 'tsla:usdt', 'BUY', '100000000000000000',
                                       '100000000000000000000000000000000', 10)
        print(tx_response)

if __name__ == '__main__':
    unittest.main()
