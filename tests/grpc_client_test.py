import unittest

from eth_account import Account

from fx_py_sdk import wallet
from fx_py_sdk.grpc_client import GRPCClient
from fx_py_sdk.builder import TxBuilder
from fx_py_sdk.codec.cosmos.base.v1beta1.coin_pb2 import Coin
from fx_py_sdk.codec.fx.dex.v1.order_pb2 import *
import decimal
from fx_py_sdk.codec.cosmos.tx.v1beta1.service_pb2 import BROADCAST_MODE_BLOCK, BROADCAST_MODE_SYNC
from google.protobuf.json_format import MessageToJson
import json

from fx_py_sdk.ibc_transfer import ConfigsKeys, Ibc_transfer

client = GRPCClient('44.196.199.119:9190')
# client = GRPCClient('127.0.0.1:9090')
pair_id = "BTC:USDT"

class MyTestCase(unittest.TestCase):

    def test_query_balances(self):
        balances = client.query_all_balances(
            address="0x8464Cf197E0e577df711edF707763Be7DAE235A6")
        print(balances)

        balances = client.query_all_balances(
            address="0x61bd2030908d658dd5a2139D2C13Af55b9138efb")
        print(balances)

    def test_query_balance(self):
        balance = client.query_balance(
            address="0x8464Cf197E0e577df711edF707763Be7DAE235A6", denom="FX")
        print(balance)

        balances = client.query_balance(
            address="0x61bd2030908d658dd5a2139D2C13Af55b9138efb", denom="FX")
        print(balances)

    def test_query_gas_price(self):
        res = client.query_gas_price()
        print(res)

    def test_query_account(self):
        account = client.query_account_info(
            address="0x61bd2030908d658dd5a2139D2C13Af55b9138efb")
        print(account)

    def test_query_oracle_price(self):
        oracle_price = client.query_oracle_price(pair_id="BTC:USDT")
        print(oracle_price)

    def test_query_positions(self):
        positions = client.query_positions(
            owner='0x61bd2030908d658dd5a2139D2C13Af55b9138efb', pair_id=pair_id)
        print("positions: ", positions)
        # owner = Address(resp.positions[0].owner)
        # print(owner.to_string())

    def test_query_order(self):
        resp = client.query_order(order_id='ID-5878-1')
        print(resp)

    def test_query_orders(self):
        resp = client.query_orders(owner="0x61bd2030908d658dd5a2139D2C13Af55b9138efb", pair_id=pair_id,
                                   page=b"1".decode('utf-8'), limit=b"20".decode('utf-8'))
        print(resp)

    def test_query_funding_info(self):
        resp = client.query_funding_info()
        print(resp)

    def test_query_funding_rates(self):
        resp = client.query_funding_rate(pair_id, 4, query_all=True)
        print(resp)

    def test_mark_price(self):
        resp = client.query_mark_price(pair_id=pair_id, query_all=True)
        print(resp)

    def test_query_orderbook(self):
        resp = client.query_orderbook(pair_id=pair_id)
        print(resp)

    def test_query_orders_by_account(self):
        orders = client.query_orders_by_account(
            '0x61bd2030908d658dd5a2139D2C13Af55b9138efb', 1, 20)
        print(orders)

    def test_create_order(self):
        Account.enable_unaudited_hdwallet_features()
        account = Account.from_mnemonic(
        "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt")
        print(account.address)

        chain_id = client.query_chain_id()
        print('chain_id:', chain_id)

        account_info = client.query_account_info(account.address)
        print('account number:', account_info.account_number,
              'sequence:', account_info.sequence)

        tx_builder = TxBuilder(account, chain_id, account_info.account_number, Coin(
            amount='600', denom='USDT'))

        tx_response = client.create_order(tx_builder, 'BTC:USDT', "SELL", decimal.Decimal(
            40000.1), decimal.Decimal(1.2), 5, account_info.sequence, mode=BROADCAST_MODE_BLOCK)
        print(MessageToJson(tx_response))

    def test_cancel_order(self):
        Account.enable_unaudited_hdwallet_features()
        account = Account.from_mnemonic(
            "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt")

        chain_id = client.query_chain_id()
        print('chain_id:', chain_id)

        account_info = client.query_account_info(account.address)
        print('account number:', account_info.account_number,
              'sequence:', account_info.sequence)

        tx_builder = TxBuilder(account, chain_id, account_info.account_number, Coin(
            amount='600', denom='USDT'))

        create_tx_response = client.create_order(tx_builder, 'BTC:USDT', BUY, decimal.Decimal(
            1.1), decimal.Decimal(1.2), 5, account_info.sequence, mode=BROADCAST_MODE_BLOCK)
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

        tx_response = client.cancel_order(
            tx_builder, order_id, account_info.sequence + 1, mode=BROADCAST_MODE_BLOCK)
        print(tx_response)

    def test_close_position(self):
        Account.enable_unaudited_hdwallet_features()
        account = Account.from_mnemonic(
            "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt")

        chain_id = client.query_chain_id()
        print('chain_id:', chain_id)

        account_info = client.query_account_info(account.address)
        print('account number:', account_info.account_number,
              'sequence:', account_info.sequence)
        print(account.address)
        positions = client.query_positions(owner=account.address, pair_id=pair_id)
        print("positions: ", positions)
        if len(positions) == 0:
            print("please build position first")
        self.assertNotEqual(len(positions), 0)

        tx_builder = TxBuilder(account, chain_id, account_info.account_number, Coin(
            amount='600', denom='USDT'))

        tx_response = client.close_position(tx_builder, pair_id, positions[0].Id, positions[0].MarkPrice, decimal.Decimal(
            0.1), True, account_info.sequence, mode=BROADCAST_MODE_BLOCK)
        print(tx_response)

    def test_add_margin(self):
        Account.enable_unaudited_hdwallet_features()
        account = Account.from_mnemonic(
            "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt")

        chain_id = client.query_chain_id()
        print('chain_id:', chain_id)

        account_info = client.query_account_info(account.address)
        print('account number:', account_info.account_number,
              'sequence:', account_info.sequence)
        print(account.address)
        positions = client.query_positions(owner=account.address, pair_id=pair_id)
        print("positions: ", positions)
        if len(positions) == 0:
            print("please build position first")
        self.assertNotEqual(len(positions), 0)

        tx_builder = TxBuilder(account, chain_id, account_info.account_number, Coin(
            amount='600', denom='USDT'))

        tx_response = client.add_margin(tx_builder, pair_id, positions[0].Id, decimal.Decimal(0.1),
                                        account_info.sequence, mode=BROADCAST_MODE_BLOCK)
        print(tx_response)


    def test_ibc_transfer_DexToFxCore(self):
        Account.enable_unaudited_hdwallet_features()
        account = Account.from_mnemonic(
            "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt")

        header = client.get_latest_block()

        account_info = client.query_account_info(account.address)
        print('account number:', account_info.account_number,
              'sequence:', account_info.sequence)
        print(account.address)

        tx_builder = TxBuilder(account,
                               None,
                               header.chain_id,
                               account_info.account_number,
                               Coin(amount='600', denom='USDT'))
        ibc_conf = Ibc_transfer()

        tx_response = client.ibc_transfer(tx_builder,
                                          ibc_conf.cfg[ConfigsKeys.IBC_CHANNELS][ConfigsKeys.BTC_FXCore],
                                          decimal.Decimal(0.1),
                                        "0xd5456f7BFeEB0AC09B73357d960B64A854Da550c",
                                          "USDT",
                                          account_info.sequence,
                                          mode=BROADCAST_MODE_BLOCK)
        print(tx_response)

    # dex-btc  -> f(x) -> dex-spy
    def test_ibc_transfer_DexToDex(self):
        Account.enable_unaudited_hdwallet_features()
        account = Account.from_mnemonic(
            "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt")

        header = client.get_latest_block()

        account_info = client.query_account_info(account.address)
        print('account number:', account_info.account_number,
              'sequence:', account_info.sequence,
              'address:', account_info.address)

        tx_builder = TxBuilder(account,
                               None,
                               header.chain_id,
                               account_info.account_number,
                               Coin(amount='600', denom='USDT'))

        priv_key = wallet.seed_to_privkey(
            "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt")

        fx_address = priv_key.to_address()
        ibc_conf = Ibc_transfer()
        receiver = '{}|transfer/{}:{}'.format(fx_address,
                                              ibc_conf.cfg[ConfigsKeys.IBC_CHANNELS][ConfigsKeys.FXCore_SPY],
                                              account.address)
        print(receiver)
        tx_response = client.ibc_transfer(tx_builder,
                                          ibc_conf.cfg[ConfigsKeys.IBC_CHANNELS][ConfigsKeys.BTC_FXCore],
                                          decimal.Decimal(0.1), receiver, "USDT",
                                          account_info.sequence, mode=BROADCAST_MODE_BLOCK)
        print(tx_response)

    def test_ibc_transfer_fromFxcoreToBTC_FX(self):
        Account.enable_unaudited_hdwallet_features()

        clientFX = GRPCClient('3.210.229.34:9090')

        priv_key = wallet.seed_to_privkey(
            "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt")

        header = clientFX.get_latest_block()
        addressFx = priv_key.to_public_key().to_address()
        account_info = clientFX.query_account_info(addressFx)
        print('account number:', account_info.account_number,
              'sequence:', account_info.sequence,
              'address:', addressFx)

        balance = clientFX.query_all_balances(addressFx)
        print('balance:', balance)

        tx_builder = TxBuilder(None,
                               priv_key,
                               header.chain_id,
                               account_info.account_number,
                               Coin(amount='20000000000000000000', denom='FX'))
        ibc_conf = Ibc_transfer()
        channel = ibc_conf.cfg[ConfigsKeys.IBC_CHANNELS][ConfigsKeys.FXCore_BTC]
        print(channel)
        tx_response = clientFX.ibc_transfer(tx_builder, channel, decimal.Decimal(1.1),
                                        "0xd5456f7BFeEB0AC09B73357d960B64A854Da550c", "FX",
                                          account_info.sequence, mode=BROADCAST_MODE_BLOCK)
        print(tx_response)

    def test_ibc_transfer_fromFxcoreToBTC_USDT(self):
        Account.enable_unaudited_hdwallet_features()

        clientFX = GRPCClient('3.210.229.34:9090')

        priv_key = wallet.seed_to_privkey(
            "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt")

        header = clientFX.get_latest_block()
        addressFx = priv_key.to_public_key().to_address()
        account_info = clientFX.query_account_info(addressFx)
        print('account number:', account_info.account_number,
              'sequence:', account_info.sequence,
              'address:', addressFx)

        balance = clientFX.query_all_balances(addressFx)
        print('balance:', balance)

        tx_builder = TxBuilder(None,
                               priv_key,
                               header.chain_id,
                               account_info.account_number,
                               Coin(amount='20000000000000000000', denom='FX'))
        ibc_conf = Ibc_transfer()
        channel = ibc_conf.cfg[ConfigsKeys.IBC_CHANNELS][ConfigsKeys.FXCore_BTC]
        print(channel)
        tx_response = clientFX.ibc_transfer(tx_builder, channel, decimal.Decimal(1.1),
                                        "0xd5456f7BFeEB0AC09B73357d960B64A854Da550c", "USDT",
                                          account_info.sequence, mode=BROADCAST_MODE_BLOCK)
        print(tx_response)

if __name__ == '__main__':
    unittest.main()
