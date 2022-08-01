import unittest
from eth_account import Account
from fx_py_sdk import wallet
from fx_py_sdk.grpc_client import GRPCClient
from fx_py_sdk.builder import TxBuilder
from fx_py_sdk.codec.cosmos.base.v1beta1.coin_pb2 import Coin
import decimal
from fx_py_sdk.codec.cosmos.tx.v1beta1.service_pb2 import BROADCAST_MODE_BLOCK, BROADCAST_MODE_SYNC

from fx_py_sdk.ibc_transfer import ConfigsKeys, Ibc_transfer

client = GRPCClient('127.0.0.1:9190')
pair_id = "BTC:USDT"

class MyTestCase(unittest.TestCase):

    def test_ibc_transfer_dex_to_fxcore(self):
        Account.enable_unaudited_hdwallet_features()
        account = Account.from_mnemonic(
            "forum welcome cute hen dance winner bubble ski actor neutral usage cherry bullet play collect shift peasant step private grow arrive fade early alarm")

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

        priv_key = wallet.seed_to_privkey(
            "forum welcome cute hen dance winner bubble ski actor neutral usage cherry bullet play collect shift peasant step private grow arrive fade early alarm")

        fx_address = priv_key.to_address()
        print(fx_address)
        tx_response = client.ibc_transfer(tx_builder,
                                          ibc_conf.cfg[ConfigsKeys.IBC_CHANNELS][ConfigsKeys.BTC_FXCore],
                                          decimal.Decimal(1),
                                          fx_address,
                                          "USDT",
                                          account_info.sequence,
                                          mode=BROADCAST_MODE_BLOCK)
        print(tx_response)

    # dex-btc -> fxcore -> dex-spy
    def test_ibc_transfer_dex_to_dex(self):

        for chain in ConfigsKeys.GRPC_List:
            if chain == "AAPL":
                to_chain = chain + "_FXCore"
                print(to_chain)
                Account.enable_unaudited_hdwallet_features()
                account = Account.from_mnemonic(
                    "forum welcome cute hen dance winner bubble ski actor neutral usage cherry bullet play collect shift peasant step private grow arrive fade early alarm")

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
                    "forum welcome cute hen dance winner bubble ski actor neutral usage cherry bullet play collect shift peasant step private grow arrive fade early alarm")

                fx_address = priv_key.to_address()
                ibc_conf = Ibc_transfer()
                receiver = '{}|transfer/{}:{}'.format(fx_address,
                                                      ibc_conf.cfg[ConfigsKeys.IBC_CHANNELS][ConfigsKeys.FXCore_AAPL],
                                                      account.address)
                print(receiver)
                tx_response = client.ibc_transfer(tx_builder,
                                                  ibc_conf.cfg[ConfigsKeys.IBC_CHANNELS][to_chain],
                                                  decimal.Decimal(10), receiver, "USDT",
                                                  account_info.sequence, mode=BROADCAST_MODE_BLOCK)
                print(tx_response)

    def test_ibc_transfer_fxcore_to_dex_fx(self):
        Account.enable_unaudited_hdwallet_features()

        clientFX = GRPCClient(ConfigsKeys.GRPC)

        priv_key = wallet.seed_to_privkey(
            "forum welcome cute hen dance winner bubble ski actor neutral usage cherry bullet play collect shift peasant step private grow arrive fade early alarm")

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
                               Coin(amount='200000000', denom='FX'))
        ibc_conf = Ibc_transfer()
        channel = ibc_conf.cfg[ConfigsKeys.IBC_CHANNELS][ConfigsKeys.FXCore_BTC]
        print(channel)
        tx_response = clientFX.ibc_transfer(tx_builder, channel, decimal.Decimal(1.1),
                                            "0xF48DF2739495e30949f8985a0cF1e47BDd927123", "FX",
                                            account_info.sequence, mode=BROADCAST_MODE_BLOCK)
        print(tx_response)

    def test_ibc_transfer_fxcore_to_dex_usdt(self):
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

    def test_transfer_to_one_chain(self):
        ibc = Ibc_transfer()
        mnemonic = "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt"

        ibc.transfer_to_one_chain(mnemonic, "USDT", "0xA1FD17f3624B64cE5Cd0d6Ed22298340488507d3", ConfigsKeys.SPY)

