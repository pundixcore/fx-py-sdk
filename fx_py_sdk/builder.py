from fx_py_sdk.codec.cosmos.tx.v1beta1.tx_pb2 import Fee
from fx_py_sdk.codec.cosmos.tx.v1beta1.tx_pb2 import ModeInfo
from fx_py_sdk.codec.cosmos.tx.v1beta1.tx_pb2 import AuthInfo
from fx_py_sdk.codec.cosmos.tx.v1beta1.tx_pb2 import SignDoc
from fx_py_sdk.codec.cosmos.tx.v1beta1.tx_pb2 import SignerInfo
from fx_py_sdk.codec.cosmos.tx.v1beta1.tx_pb2 import Tx
from fx_py_sdk.codec.cosmos.tx.v1beta1.tx_pb2 import TxBody
from fx_py_sdk.codec.cosmos.base.v1beta1.coin_pb2 import Coin
from fx_py_sdk.codec.cosmos.tx.signing.v1beta1.signing_pb2 import SIGN_MODE_DIRECT
from google.protobuf.any_pb2 import Any
from fx_py_sdk.wallet import PrivateKey, Address

DEFAULT_DENOM = "FX"


class TxBuilder:
    def __init__(self, private_key: PrivateKey,
                 chain_id: str = '',
                 account_number: int = -1,
                 gas_price: Coin = Coin(amount='0', denom=DEFAULT_DENOM)):
        self.chain_id = chain_id
        self.account_number = account_number
        if gas_price.denom == '':
            raise Exception('gas price denom can not be empty')
        self.gas_price = gas_price
        self._private_key = private_key
        self._memo = ''

    def with_memo(self, memo: str):
        self._memo = memo

    def address(self) -> str:
        return self._private_key.to_address()

    def acc_address(self):
        addr = Address(self.address())
        return addr.to_bytes()

    def sign(self, sequence: int, msgs: [Any], fee: Fee, timeout_height: int = 0) -> Tx:
        tx_body = TxBody(messages=msgs, memo=self._memo, timeout_height=timeout_height)
        tx_body_bytes = tx_body.SerializeToString()

        single = ModeInfo.Single(mode=SIGN_MODE_DIRECT)
        mode_info = ModeInfo(single=single)
        pub_key_any = self._private_key.to_public_key().to_secp256k1_any()

        signer_info = SignerInfo(public_key=pub_key_any, mode_info=mode_info, sequence=sequence)
        auth_info = AuthInfo(signer_infos=[signer_info], fee=fee)
        auth_info_bytes = auth_info.SerializeToString()

        sign_doc = SignDoc(body_bytes=tx_body_bytes,
                           auth_info_bytes=auth_info_bytes,
                           chain_id=self.chain_id,
                           account_number=self.account_number)
        sign_doc_bytes = sign_doc.SerializeToString()
        signature = self._private_key.sign(sign_doc_bytes)
        return Tx(body=tx_body, auth_info=auth_info, signatures=[signature])