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
from fx.dex.tx_pb2_grpc import MsgStub
from fx.dex.tx_pb2 import *

import bech32

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

    # 查询仓位
    #   owner: 仓位持有人
    #   pair_id: 交易对
    def query_positions(self, owner, pair_id):
        hrp, data = bech32.bech32_decode(owner)
        converted = bech32.convertbits(data, 5, 8, False)
        response = DexQuery(self.channel).QueryPosition(QueryPositionReq(owner=bytes(converted), pair_id=pair_id))
        return response

    # 查询订单
    #   owner: 仓位持有地址
    #   pair_id: 交易对
    def query_order(self,order_id):
        response = DexQuery(self.channel).QueryOrder(QueryOrderRequest(order_id=order_id))
        return response

    # 根据地址和交易对查询订单
    #   owner: 仓位持有地址
    #   pair_id: 交易对
    def query_orders(self, owner, pair_id, page, limit):
        hrp, data = bech32.bech32_decode(owner)
        converted = bech32.convertbits(data, 5, 8, False)
        response = DexQuery(self.channel).QueryOrders(QueryOrdersRequest(
            owner=converted, pair_id=pair_id, page=page, limit=limit))
        return response

    # 查询资金费率
    #   无需传参
    def query_funding(self):
        response = DexQuery(self.channel).QueryFunding(QueryFundingReq())
        return response

    # 查询标记价格
    #   pair_id: 交易对
    #   query_all: 是否查询全部
    def query_mark_price(self, pair_id, query_all):
        response = DexQuery(self.channel).QueryMarkPrice(QueryMarkPriceReq(pair_id=pair_id, query_all=query_all))
        return response


    def create_order(self, priv_key, account_number, account_seq, chain_id,
                     owner, pair_id, direction, price, base_quantity, leverage):
        msg = MsgCreateOrder(owner=owner, pair_id=pair_id, direction=direction, price=price, base_quantity=base_quantity,
                                  ttl=1000, leverage=leverage)
        print("msg: ", msg)
        msg_any = Any(type_url='/fx.dex.MsgCreateOrder', value=msg.SerializeToString())
        tx_builder = TxBuilder(priv_key, chain_id, account_number)
        tx = tx_builder.sign(account_seq, [msg_any])
        tx = self.build_tx(tx_builder, [msg_any])
        print('====', tx)
        tx_response = self.broadcast_tx(tx)
        print(tx_response)
        return tx_response

    def cancel_order(self, cli, priv_key, account_number, account_seq, chain_id,
                     owner, order_id):
        msg = MsgCancelOrder(owner=owner, pair_id=order_id)
        msg_any = Any(type_url='/fx.dex.MsgCancelOrder', value=msg.SerializeToString())
        tx_builder = TxBuilder(priv_key, chain_id, account_number)
        tx = tx_builder.sign(account_seq, [msg_any])
        tx = self.build_tx(tx_builder, [msg_any])
        tx_response = self.broadcast_tx(tx)
        print(tx_response)
        return tx_response

    def close_position(self, cli, priv_key, account_number, account_seq, chain_id,
                       owner, pair_id, position_id, price, base_quantity):
        msg = MsgClosePosition(owner=owner, pair_id=pair_id, position_id=position_id, price=price, base_quantity=base_quantity)
        msg_any = Any(type_url='/fx.dex.MsgClosePosition', value=msg.SerializeToString())
        tx_builder = TxBuilder(priv_key, chain_id, account_number)
        tx = tx_builder.sign(account_seq, [msg_any])
        tx = self.build_tx(tx_builder, [msg_any])
        tx_response = cli.broadcast_tx(tx)
        print(tx_response)
        return tx_response

    def build_tx(self, tx_builder: TxBuilder, msg: [Any], gas_limit: int = 0) -> Tx:
        if tx_builder.chain_id == 'fxdex':
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

        # fee_amount = Coin(amount=, denom=fee_denom)
        # fee = Fee(amount=[fee_amount], gas_limit=gas_limit)
        # tx = tx_builder.sign(account.sequence, msg, fee)
        # gas_info = self.estimating_gas(tx)
        # gas_limit = int(float(gas_info.gas_used) * 1.5)
        fee_amount = Coin(amount='300000000000000', denom=fee_denom)
        fee = Fee(amount=[fee_amount], gas_limit=200000)
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
