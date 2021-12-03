import grpc

from cosmos.auth.v1beta1.auth_pb2 import BaseAccount
from cosmos.auth.v1beta1.query_pb2 import QueryAccountRequest
from cosmos.auth.v1beta1.query_pb2_grpc import QueryStub as AuthQuery
from cosmos.bank.v1beta1.query_pb2 import QueryAllBalancesRequest
from cosmos.bank.v1beta1.query_pb2 import QueryBalanceRequest
from cosmos.bank.v1beta1.query_pb2_grpc import QueryStub as BankQuery
from cosmos.base.tendermint.v1beta1.query_pb2 import GetBlockByHeightRequest
from cosmos.base.tendermint.v1beta1.query_pb2_grpc import ServiceStub as TendermintClient
from cosmos.base.v1beta1.coin_pb2 import Coin
from fx.other.query_pb2 import GasPriceRequest
from fx.other.query_pb2_grpc import QueryStub as OtherQuery

from fx.dex.query_pb2_grpc import QueryStub as DexQuery
from fx.dex.query_pb2 import *


def query_account_info(channel: grpc.Channel, address: str) -> BaseAccount:
    """查询用户信息"""
    response = AuthQuery(channel).Account(QueryAccountRequest(address=address))
    # Any 类型转换 - BaseAccount
    base_account = BaseAccount()
    response.account.Unpack(base_account)
    return base_account


def query_all_balances(channel: grpc.Channel, address: str) -> [Coin]:
    """查询用户所有的余额"""
    response = BankQuery(channel).AllBalances(QueryAllBalancesRequest(address=address))
    return response.balances

def query_balance(channel: grpc.Channel, address: str, denom: str) -> Coin:
    response = BankQuery(channel).Balance(QueryBalanceRequest(address=address, denom=denom))
    return response.balance


def get_gas_price(channel: grpc.Channel) -> [Coin]:
    response = OtherQuery(channel).GasPrice(GasPriceRequest())
    return response.gas_prices

def get_chain_id(channel: grpc.Channel) -> str:
    response = TendermintClient(channel).GetLatestBlock(GetBlockByHeightRequest())
    return response.block.header.chain_id

def query_all_positions(channel: grpc.Channel, owner, pair_id):
    response = DexQuery(channel).QueryPosition(QueryPositionReq(owner=owner, pair_id=pair_id))
    return response


