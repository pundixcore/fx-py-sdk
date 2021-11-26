from builder import TxBuilder
from grpc_client import GRPCClient
import wallet
from cosmos.bank.v1beta1.tx_pb2 import MsgSend
from cosmos.base.v1beta1.coin_pb2 import Coin
from google.protobuf.any_pb2 import Any


def test_send_tx():
    priv_key = wallet.seed_to_privkey(
        'lonely trumpet tiny soccer brief holiday eye warm credit focus correct april between '
        'armed spoon dice save visit endorse wonder record swim course field')
    address = priv_key.to_address()
    print('address:', address)

    cli = GRPCClient('127.0.0.1:9090')
    chain_id = cli.query_chain_id()
    print('chain_id:', chain_id)

    account = cli.query_account_info(address)
    print('account, number:', account.account_number, 'sequence:', account.sequence)

    send_msg = MsgSend(from_address=address, to_address=address, amount=[Coin(amount='100', denom='FX')])
    print(send_msg)
    send_msg_any = Any(type_url='/cosmos.bank.v1beta1.MsgSend', value=send_msg.SerializeToString())

    tx_builder = TxBuilder(priv_key, chain_id, account.account_number)
    tx = tx_builder.sign(account.sequence, [send_msg_any])
    print(tx)
    print(tx.signatures[0].hex())

    tx = cli.build_tx(tx_builder, [send_msg_any])
    print(tx)
    print(tx.signatures[0].hex())
    tx_response = cli.broadcast_tx(tx)
    print(tx_response)


if __name__ == '__main__':
    test_send_tx()
