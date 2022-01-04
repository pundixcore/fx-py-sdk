import unittest
from fx_py_sdk import wallet
from fx_py_sdk.wallet import Address
from fx_py_sdk.grpc_client import GRPCClient, DEFAULT_GRPC_NONE, DEFAULT_DEC
from fx_py_sdk.builder import TxBuilder
from fx_py_sdk.codec.cosmos.base.v1beta1.coin_pb2 import Coin
from fx_py_sdk.codec.fx.dex.order_pb2 import *
import decimal
from fx_py_sdk.codec.cosmos.tx.v1beta1.service_pb2 import BROADCAST_MODE_BLOCK, BROADCAST_MODE_SYNC
from google.protobuf.json_format import MessageToJson
import json
from google.protobuf.timestamp_pb2 import Timestamp

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

    def test_query_oracle_price(self):
        oracle_price = client.query_oracle_price(pair_id="tsla:usdt")
        print(oracle_price)

    def test_query_positions(self):
        positions = client.query_positions(owner='dex179q82e7fcck4ftfvf4vfpwkg86jmxf7upext3v', pair_id="tsla:usdt")
        print("positions: ", positions)
        # owner = Address(resp.positions[0].owner)
        # print(owner.to_string())

    def test_query_order(self):
        resp = client.query_order(order_id='ID-429928-2')
        print(resp)

    def test_query_orders(self):
        resp = client.query_orders(owner="dex1ggz598a4506llaglzsmhp3r23hfke6nw29wans", pair_id="tsla:usdc",
                                   page=b"1".decode('utf-8'), limit=b"20".decode('utf-8'))
        print(resp)

    def test_query_funding_info(self):
        resp = client.query_funding_info()
        print(resp)

    def test_query_funding_rates(self):
        resp = client.query_funding_rate("tsla:usdt", 4, query_all=True)
        print(resp)

    def test_mark_price(self):
        resp = client.query_mark_price(pair_id="tsla:usdt", query_all=True)
        print(resp)

    def test_query_orderbook(self):
        resp = client.query_orderbook(pair_id="tsla:usdt")
        print(resp)

    def test_query_funding_rate_log(self):
        resp = client.query_funding_rate_log(pair_id="tsla:usdt")
        print(resp)

    def test_create_order(self):
        priv_key = wallet.seed_to_privkey(
            "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt")

        address = priv_key.to_address()
        print('address:', address)

        chain_id = client.query_chain_id()
        print('chain_id:', chain_id)

        account = client.query_account_info(address)
        print('account number:', account.account_number, 'sequence:', account.sequence)

        tx_builder = TxBuilder(priv_key, chain_id, account.account_number, Coin(amount='60000000', denom='FX'))

        tx_response = client.create_order(tx_builder, 'tsla:usdt', "BUY", decimal.Decimal(910.1), decimal.Decimal(1.2), 10, account.sequence, mode=BROADCAST_MODE_BLOCK)
        print(MessageToJson(tx_response))

    def test_cancel_order(self):
        priv_key = wallet.seed_to_privkey(
            "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt")

        address = priv_key.to_address()
        print('address:', address)

        chain_id = client.query_chain_id()
        print('chain_id:', chain_id)

        account = client.query_account_info(address)
        print('account number:', account.account_number, 'sequence:', account.sequence)

        tx_builder = TxBuilder(priv_key, chain_id, account.account_number, Coin(amount='60000000', denom='FX'))

        create_tx_response = client.create_order(tx_builder, 'tsla:dai', BUY, decimal.Decimal(1.1), decimal.Decimal(1.2), 10, account.sequence, mode=BROADCAST_MODE_BLOCK)
        res_str = MessageToJson(create_tx_response)
        res = json.loads(res_str)
        order_id = ''
        events = res['logs'][0]['events']
        for event in events:
            if event['type'] == 'fx.dex.Order':
                for attribute in event['attributes']:
                    if attribute['key'] == 'order_id':
                        order_id = attribute['value']

        print("create order id = ", order_id)

        tx_response = client.cancel_order(tx_builder, order_id, account.sequence + 1, mode=BROADCAST_MODE_BLOCK)
        print(tx_response)

    def test_close_position(self):
        pair_id = "tsla:usdt"
        priv_key = wallet.seed_to_privkey(
            "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt")

        address = priv_key.to_address()
        print('address:', address)

        chain_id = client.query_chain_id()
        print('chain_id:', chain_id)

        account = client.query_account_info(address)
        print('account number:', account.account_number, 'sequence:', account.sequence)

        positions = client.query_positions(owner='dex1zgpzdf2uqla7hkx85wnn4p2r3duwqzd8cfus97', pair_id=pair_id)
        print("positions: ", positions)
        self.assertNotEqual(len(positions), 0)

        tx_builder = TxBuilder(priv_key, chain_id, account.account_number, Coin(amount='60000000', denom='FX'))
        tx_response = client.close_position(tx_builder, pair_id, positions[0].Id, positions[0].MarkPrice, decimal.Decimal(0.1), True, account.sequence, mode=BROADCAST_MODE_BLOCK)
        print(tx_response)

    def test_query_orders_by_account(self):
        orders = client.query_orders_by_account('dex1n58mly6f7er0zs6swtetqgfqs36jaarqlhs528', 1, 20)
        print(orders)

    def test_decimal(self):
        base_quantity = decimal.Decimal('1.281999999999997730')
        base_quantity = base_quantity * decimal.Decimal(DEFAULT_DEC)
        base_quantity = str(base_quantity)
        base_quantity_split = base_quantity.split('.', 1)
        print(base_quantity_split)

    def test_decimal_neg(self):
        base_quantity = decimal.Decimal('-1.281999999999997730')
        base_quantity = base_quantity * decimal.Decimal(DEFAULT_DEC)
        base_quantity = str(base_quantity)
        base_quantity_split = base_quantity.split('.', 1)
        print(base_quantity_split)

    def test_proto_time(self):
        time1 = "2021-12-24T07:09:12.504154Z"
        time2 = Timestamp()
        time2.FromJsonString(time1)
        print(time2)
        time3 = Timestamp().FromJsonString(time1) #return None
        print(time3)

if __name__ == '__main__':
    unittest.main()
