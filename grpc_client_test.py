import unittest
import wallet
from wallet import Address
from grpc_client import GRPCClient
from builder import TxBuilder
from cosmos.base.v1beta1.coin_pb2 import Coin

client = GRPCClient('44.196.199.119:9090')


class MyTestCase(unittest.TestCase):

    def test_query_balances(self):
        balances = client.query_all_balances(address="dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy")
        print(balances)

    def test_query_balance(self):
        balances = client.query_balance(address="dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy", denom="FX")
        print(balances)

    def test_query_gas_price(self):
        res = client.query_gas_price()
        print(res)

    def test_query_account(self):
        account = client.query_account_info(address="dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy")
        print(account)

    def test_query_positions(self):
        resp = client.query_positions(owner='dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy', pair_id="tsla:usdt")
        print(resp)
        owner = Address(resp.positions[0].owner)
        print(owner.to_string())

    def test_query_order(self):
        resp = client.query_order(order_id='ID-880797-1')
        print(resp)

    def test_query_orders(self):
        resp = client.query_orders(owner="dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy", pair_id="tsla:usdt",
                                   page=b"1".decode('utf-8'), limit=b"20".decode('utf-8'))
        print(resp)

    def test_query_funding(self):
        resp = client.query_funding()
        print(resp)

    def test_mark_price(self):
        resp = client.query_mark_price(pair_id="tsla:usdt", query_all=True)
        print(resp)

    def test_create_order(self):
        cli = GRPCClient('44.196.199.119:9090')

        priv_key = wallet.seed_to_privkey(
            "sunset earth lab edit usage hire night today nurse swap bubble summer trigger improve nice shrimp brown jaguar uncover affair wood envelope bar pear")

        address = priv_key.to_address()
        print('address:', address)

        chain_id = cli.query_chain_id()
        print('chain_id:', chain_id)

        account = cli.query_account_info(address)
        print('account number:', account.account_number, 'sequence:', account.sequence)

        tx_builder = TxBuilder(priv_key, chain_id, account.account_number, Coin(amount='60000000', denom='FX'))

        tx_response = cli.create_order(tx_builder, 'tsla:usdt', 'BUY', '100000000000000000',
                                       '100000000000000000000000000', 10)
        print(tx_response)

    def test_cancel_order(self):
        cli = GRPCClient('44.196.199.119:9090')

        priv_key = wallet.seed_to_privkey(
            "sunset earth lab edit usage hire night today nurse swap bubble summer trigger improve nice shrimp brown jaguar uncover affair wood envelope bar pear")

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
            "sunset earth lab edit usage hire night today nurse swap bubble summer trigger improve nice shrimp brown jaguar uncover affair wood envelope bar pear")

        address = priv_key.to_address()
        print('address:', address)

        chain_id = cli.query_chain_id()
        print('chain_id:', chain_id)

        account = cli.query_account_info(address)
        print('account number:', account.account_number, 'sequence:', account.sequence)

        tx_builder = TxBuilder(priv_key, chain_id, account.account_number, Coin(amount='60000000', denom='FX'))

        tx_response = cli.close_position(tx_builder, "tsla:usdt", "1593", "100", "1765981856000000000000")
        print(tx_response)


if __name__ == '__main__':
    unittest.main()
