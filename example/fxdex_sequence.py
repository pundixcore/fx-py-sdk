from eth_account import Account
from fx_py_sdk.grpc_client import GRPCClient
from fx_py_sdk.builder import TxBuilder
from fx_py_sdk.codec.cosmos.base.v1beta1.coin_pb2 import Coin
import decimal
from fx_py_sdk.codec.cosmos.tx.v1beta1.service_pb2 import BROADCAST_MODE_BLOCK, BROADCAST_MODE_SYNC
from google.protobuf.json_format import MessageToJson

def main():
    client = GRPCClient('127.0.0.1:9090')

    Account.enable_unaudited_hdwallet_features()
    account = Account.from_mnemonic(
        "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt")
    print(account.address)

    chain_id = client.query_chain_id()
    print('chain_id:', chain_id)

    account_info = client.query_account_info(account.address)
    print('account number:', account_info.account_number,
          'sequence:', account_info.sequence)

    tx_builder = TxBuilder(account, None, chain_id, account_info.account_number, Coin(
        amount='600', denom='USDT'))

    account_info = client.query_account_info(account.address)
    print('account number:', account_info.account_number,
          'sequence:', account_info.sequence)
    sequence =  account_info.sequence
    for i in range (0, 100):
        tx_response = client.create_order(tx_builder, 'TSLA:USDT', "SELL", decimal.Decimal(
            900), decimal.Decimal(1.2), 5, sequence, mode=BROADCAST_MODE_SYNC)
        res_str = MessageToJson(tx_response)
        sequence = sequence + 1
        print(res_str)


if __name__ == "__main__":
    main()