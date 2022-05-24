import decimal

import yaml
from eth_account import Account
from fx_py_sdk.codec.cosmos.tx.v1beta1.service_pb2 import BROADCAST_MODE_BLOCK

from fx_py_sdk.codec.cosmos.base.v1beta1.coin_pb2 import Coin

from fx_py_sdk import wallet
from fx_py_sdk.builder import TxBuilder

from fx_py_sdk.grpc_client import GRPCClient

class ConfigsKeys:
    IBC_CHANNELS = "IBC_CHANNELS"
    TSLA_FXCore = "TSLA_FXCore"
    FXCore_TSLA = "FXCore_TSLA"

    AAPL_FXCore = "AAPL_FXCore"
    FXCore_AAPL = "FXCore_AAPL"

    NFLX_FXCore = "NFLX_FXCore"
    FXCore_NFLX = "FXCore_NFLX"

    GOOG_FXCore = "GOOG_FXCore"
    FXCore_GOOG = "FXCore_GOOG"

    FB_FXCore = "FB_FXCore"
    FXCore_FB = "FXCore_FB"

    AMZ_FXCore = "AMZ_FXCore"
    FXCore_AMZ = "FXCore_AMZ"

    BTC_FXCore = "BTC_FXCore"
    FXCore_BTC = "FXCore_BTC"

    FX_FXCore = "FX_FXCore"
    FXCore_FX = "FXCore_FX"

    SPY_FXCore = "SPY_FXCore"
    FXCore_SPY = "FXCore_SPY"

    IWM_FXCore = "IWM_FXCore"
    FXCore_IWM = "FXCore_IWM"

    TQQQ_FXCore = "TQQQ_FXCore"
    FXCore_TQQQ = "FXCore_TQQQ"

    ###########rpc##############
    RPC = "RPC"
    GRPC = "GRPC"
    GRPC_List = ["TSLA", "AAPL", "NFLX", "GOOG", "FB", "AMZN", "BTC", "FX", "SPY", "IWM", "TQQQ"]
    TSLA = "TSLA"
    AAPL = "AAPL"
    NFLX = "NFLX"
    GOOG = "GOOG"
    FB = "FB"
    AMZN = "AMZN"
    BTC = "BTC"
    FX = "FX"
    SPY = "SPY"
    IWM = "IWM"
    TQQQ = "TQQQ"

class Ibc_transfer:
    def __init__(self):
        with open("config.yaml", "r") as ymlfile:
            self.cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    def transfer_to_one_chain(self, mnemonic:str, denom:str, to_address:str, to_chain:str):
        for chain in ConfigsKeys.GRPC_List:
            url = self.cfg[ConfigsKeys.GRPC][chain]
            if len(url) > 0 and chain != to_chain:
                client = GRPCClient(url)
                Account.enable_unaudited_hdwallet_features()
                account = Account.from_mnemonic(mnemonic)

                header = client.get_latest_block()

                account_info = client.query_account_info(account.address)

                print('-------------{}-------------\nchain_url: {}\naccount number: {}\naddress: {}'.format(chain, url, account_info.account_number, account_info.address))
                balance = client.query_balance(account_info.address, denom)
                gapPrice = Coin(amount='600', denom='USDT')
                tx_builder = TxBuilder(account,
                                       None,
                                       header.chain_id,
                                       account_info.account_number,
                                       gapPrice)
                amount = balance[denom] - 1000000000000000
                print(str(amount))

                priv_key = wallet.seed_to_privkey(mnemonic)

                fx_address = priv_key.to_address()
                ibc_conf = Ibc_transfer()
                receiver = '{}|transfer/{}:{}'.format(fx_address,
                                                      ibc_conf.cfg[ConfigsKeys.IBC_CHANNELS]["FXCore_" + to_chain],
                                                      to_address)
                print('receiver:', receiver)
                tx_response = client.ibc_transfer(tx_builder,
                                                  ibc_conf.cfg[ConfigsKeys.IBC_CHANNELS][chain + "_FXCore"],
                                                  decimal.Decimal(amount), receiver, denom,
                                                  account_info.sequence, mode=BROADCAST_MODE_BLOCK)
                print(tx_response)