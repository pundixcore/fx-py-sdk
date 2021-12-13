import unittest
from fx_py_sdk import wallet
from fx_py_sdk.wallet import Address
from fx_py_sdk.grpc_client import GRPCClient, DEFAULT_GRPC_NONE
from fx_py_sdk.builder import TxBuilder
from fx_py_sdk.codec.cosmos.base.v1beta1.coin_pb2 import Coin
from fx_py_sdk.codec.fx.dex.order_pb2 import *
import decimal

client = GRPCClient('44.196.199.119:9090')
# client = GRPCClient('127.0.0.1:9090')


class MyTestCase(unittest.TestCase):
    def test_query_balances(self):
        balances = client.query_all_balances(address="dex1zgpzdf2uqla7hkx85wnn4p2r3duwqzd8cfus97")
        print(balances)

        balances = client.query_all_balances(address="dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy")
        print(balances)

    def test_query_balance(self):
        balance = client.query_balance(address="dex1waw8g8v3xw6549mvd476dvq6hwlvdry9a353ug", denom="FX")
        print(balance)

        balances = client.query_balance(address="dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy", denom="FX")
        print(balances)

    def test_query_gas_price(self):
        res = client.query_gas_price()
        print(res)

    def test_query_account(self):
        account = client.query_account_info(address="dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy")
        print(account)

    def test_query_positions(self):
        positions = client.query_positions(owner='dex1ggz598a4506llaglzsmhp3r23hfke6nw29wans', pair_id="tsla:usdt")
        print("positions: ", positions)
        # owner = Address(resp.positions[0].owner)
        # print(owner.to_string())

    def test_query_order(self):
        resp = client.query_order(order_id='ID-706-1')
        print(resp)


    def test_query_orders(self):
        resp = client.query_orders(owner="dex1ggz598a4506llaglzsmhp3r23hfke6nw29wans", pair_id="tsla:usdc",
                                   page=b"1".decode('utf-8'), limit=b"20".decode('utf-8'))
        print(resp)

    def test_query_funding_info(self):
        resp = client.query_funding_info()
        print(resp)

    def test_query_funding_rates(self):
        resp = client.query_funding_rate("tsla:usdt", 10, query_all=True)
        print(resp)

    def test_mark_price(self):
        resp = client.query_mark_price(pair_id="tsla:usdt", query_all=True)
        print(resp)

    def test_query_orderbook(self):
        resp = client.query_orderbook(pair_id="tsla:usdt")
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

        tx_response = cli.create_order(tx_builder, 'tsla:usdt', BUY, 1, 1.1, 10)
        print(tx_response)

    def test_cancel_order(self):
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
        tx_response = cli.cancel_order(tx_builder, "ID-880797-1")
        print(tx_response)

    def test_close_position(self):
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

        tx_response = cli.close_position(tx_builder, "tsla:usdt", "1593", 1, 1.1)
        print(tx_response)


if __name__ == '__main__':
    unittest.main()
