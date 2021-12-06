import grpc

from cosmos.auth.v1beta1.auth_pb2 import BaseAccount
from cosmos.auth.v1beta1.query_pb2 import QueryAccountRequest
from cosmos.auth.v1beta1.query_pb2_grpc import QueryStub as AuthQuery
from cosmos.bank.v1beta1.query_pb2 import QueryAllBalancesRequest
from cosmos.bank.v1beta1.query_pb2 import QueryBalanceRequest
from cosmos.bank.v1beta1.query_pb2_grpc import QueryStub as BankQuery
from cosmos.base.tendermint.v1beta1.query_pb2 import GetBlockByHeightRequest
from cosmos.base.tendermint.v1beta1.query_pb2_grpc import ServiceStub as TendermintClient
from cosmos.base.abci.v1beta1.abci_pb2 import GasInfo
from cosmos.base.abci.v1beta1.abci_pb2 import TxResponse
from cosmos.tx.v1beta1.service_pb2_grpc import ServiceStub as TxClient
from cosmos.tx.v1beta1.service_pb2 import SimulateRequest
from cosmos.tx.v1beta1.service_pb2 import BroadcastTxRequest
from cosmos.tx.v1beta1.service_pb2 import BroadcastMode
from cosmos.tx.v1beta1.service_pb2 import BROADCAST_MODE_BLOCK
from cosmos.tx.v1beta1.tx_pb2 import Tx
from cosmos.tx.v1beta1.tx_pb2 import TxRaw
from cosmos.tx.v1beta1.tx_pb2 import Fee
from cosmos.base.v1beta1.coin_pb2 import Coin
from fx.other.query_pb2 import GasPriceRequest
from fx.other.query_pb2_grpc import QueryStub as OtherQuery
from google.protobuf.any_pb2 import Any
from builder import TxBuilder

from fx.dex.query_pb2_grpc import QueryStub as DexQuery
from fx.dex.query_pb2 import *


class GRPCClient:
    def __init__(self, url: str = 'localhost:9090'):
        self.channel = grpc.insecure_channel(url)

    def query_account_info(self, address: str) -> BaseAccount:
        """查询账户信息"""
        response = AuthQuery(self.channel).Account(QueryAccountRequest(address=address))
        # Any 类型转换 - BaseAccount
        base_account = BaseAccount()
        response.account.Unpack(base_account)
        return base_account

    def query_all_balances(self, address: str) -> [Coin]:
        """查询所有余额"""
        response = BankQuery(self.channel).AllBalances(QueryAllBalancesRequest(address=address))
        return response.balances

    def query_balance(self, address: str, denom: str) -> Coin:
        """查询Denom对应的余额"""
        response = BankQuery(self.channel).Balance(QueryBalanceRequest(address=address, denom=denom))
        return response.balance

    def query_gas_price(self) -> [Coin]:
        """查询gas price"""
        response = OtherQuery(self.channel).GasPrice(GasPriceRequest())
        return response.gas_prices

    def query_chain_id(self) -> str:
        """查询 chain id"""
        response = TendermintClient(self.channel).GetLatestBlock(GetBlockByHeightRequest())
        return response.block.header.chain_id

    def build_tx(self, tx_builder: TxBuilder, msg: [Any], gas_limit: int = 0) -> Tx:
        if tx_builder.chain_id == '':
            tx_builder.chain_id = self.query_chain_id()

        account = self.query_account_info(tx_builder.address())
        if tx_builder.account_number <= -1:
            tx_builder.account_number = account.account_number

        gas_price_amount = 0
        fee_denom = tx_builder.gas_price.denom
        if int(tx_builder.gas_price.amount) <= 0:
            for item in self.query_gas_price():
                if item.denom == fee_denom:
                    gas_price_amount = int(item.amount)

        fee_amount = Coin(amount=str(gas_limit * gas_price_amount), denom=fee_denom)
        fee = Fee(amount=[fee_amount], gas_limit=gas_limit)
        tx = tx_builder.sign(account.sequence, msg, fee)
        gas_info = self.estimating_gas(tx)
        gas_limit = int(float(gas_info.gas_used) * 1.5)
        fee_amount = Coin(amount=str(gas_limit * gas_price_amount), denom=fee_denom)
        fee = Fee(amount=[fee_amount], gas_limit=gas_limit)
        return tx_builder.sign(account.sequence, msg, fee)

    def estimating_gas(self, tx: Tx) -> GasInfo:
        """估算交易Gas"""
        response = TxClient(self.channel).Simulate(SimulateRequest(tx=tx))
        return response.gas_info

    def broadcast_tx(self, tx: Tx, mode: BroadcastMode = BROADCAST_MODE_BLOCK) -> TxResponse:
        """广播交易"""
        tx_raw = TxRaw(body_bytes=tx.body.SerializeToString(),
                       auth_info_bytes=tx.auth_info.SerializeToString(),
                       signatures=tx.signatures)
        tx_bytes = tx_raw.SerializeToString()
        response = TxClient(self.channel).BroadcastTx(BroadcastTxRequest(tx_bytes=tx_bytes, mode=mode))
        return response.tx_response
