from fx_py_sdk.builder import TxBuilder
from fx_py_sdk.grpc_client import GRPCClient
from fx_py_sdk import wallet
from fx_py_sdk.codec.cosmos.bank.v1beta1.tx_pb2 import MsgSend
from fx_py_sdk.codec.cosmos.base.v1beta1.coin_pb2 import Coin
from google.protobuf.any_pb2 import Any

"""转账交易测试"""


def test_send_tx():
    """导入种子账户"""
    priv_key = wallet.seed_to_privkey(
        "dune antenna hood magic kit blouse film video another pioneer dilemma hobby message rug sail gas culture upgrade twin flag joke people general aunt")

    """获取账户地址"""
    address = priv_key.to_address()
    print('address:', address)

    """创建GRPC连接"""
    cli = GRPCClient('44.196.199.119:9090')

    """查询chainId"""
    chain_id = cli.query_chain_id()
    print('chain_id:', chain_id)

    """查询账户信息"""
    account = cli.query_account_info(address)
    print('account, number:', account.account_number, 'sequence:', account.sequence)

    """构造 tx_builder 对象"""
    tx_builder = TxBuilder(priv_key, chain_id, account.account_number, Coin(amount='60000000', denom='FX'))

    """构造转账交易msg"""
    send_msg = MsgSend(from_address=address, to_address=address, amount=[Coin(amount='100', denom='FX')])
    send_msg_any = Any(type_url='/cosmos.bank.v1beta1.MsgSend', value=send_msg.SerializeToString())

    """构造并签名交易"""
    tx = cli.build_tx(tx_builder, [send_msg_any], 5000000)
    print(tx)

    """广播交易"""
    tx_response = cli.broadcast_tx(tx)
    print(tx_response)


if __name__ == '__main__':
    test_send_tx()
