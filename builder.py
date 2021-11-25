import grpc

import wallet

import grpc_client


class TxBuilder:
    def __init__(self, chain_id: str, private_key: wallet.PrivateKey, account_number: int, fees_denom: str):
        self.chain_id = chain_id
        self.private_key = private_key
        self.account_number = account_number
        self.fees_denom = fees_denom
        self.memo = ''

    def with_memo(self, memo: str):
        self.memo = memo

    def address(self) -> str:
        return self.private_key.to_address()

    def get_next_sequence(self, channel: grpc.Channel) -> int:
        address=self.address()
        account = grpc_client.query_account_info(channel=channel, address=address)
        return account.sequence

    # def sign(self):
