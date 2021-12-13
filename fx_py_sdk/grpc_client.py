import decimal

import grpc

from fx_py_sdk.codec.cosmos.auth.v1beta1.auth_pb2 import BaseAccount
from fx_py_sdk.codec.cosmos.auth.v1beta1.query_pb2 import QueryAccountRequest
from fx_py_sdk.codec.cosmos.auth.v1beta1.query_pb2_grpc import QueryStub as AuthQuery
from fx_py_sdk.codec.cosmos.bank.v1beta1.query_pb2 import QueryAllBalancesRequest
from fx_py_sdk.codec.cosmos.bank.v1beta1.query_pb2 import QueryBalanceRequest
from fx_py_sdk.codec.cosmos.bank.v1beta1.query_pb2_grpc import QueryStub as BankQuery
from fx_py_sdk.codec.cosmos.base.tendermint.v1beta1.query_pb2 import GetBlockByHeightRequest
from fx_py_sdk.codec.cosmos.base.tendermint.v1beta1.query_pb2_grpc import ServiceStub as TendermintClient
from fx_py_sdk.codec.cosmos.base.abci.v1beta1.abci_pb2 import GasInfo
from fx_py_sdk.codec.cosmos.base.abci.v1beta1.abci_pb2 import TxResponse
from fx_py_sdk.codec.cosmos.tx.v1beta1.service_pb2_grpc import ServiceStub as TxClient
from fx_py_sdk.codec.cosmos.tx.v1beta1.service_pb2 import SimulateRequest
from fx_py_sdk.codec.cosmos.tx.v1beta1.service_pb2 import BroadcastTxRequest
from fx_py_sdk.codec.cosmos.tx.v1beta1.service_pb2 import BroadcastMode
from fx_py_sdk.codec.cosmos.tx.v1beta1.service_pb2 import BROADCAST_MODE_BLOCK, BROADCAST_MODE_SYNC
from fx_py_sdk.codec.cosmos.tx.v1beta1.tx_pb2 import Tx
from fx_py_sdk.codec.cosmos.tx.v1beta1.tx_pb2 import TxRaw
from fx_py_sdk.codec.cosmos.tx.v1beta1.tx_pb2 import Fee
from fx_py_sdk.codec.cosmos.base.v1beta1.coin_pb2 import Coin
from fx_py_sdk.codec.fx.other.query_pb2 import GasPriceRequest
from fx_py_sdk.codec.fx.other.query_pb2_grpc import QueryStub as OtherQuery
from google.protobuf.any_pb2 import Any
from fx_py_sdk.builder import TxBuilder

from fx_py_sdk.codec.fx.dex.query_pb2_grpc import QueryStub as DexQuery
from fx_py_sdk.codec.fx.dex.query_pb2 import *
from fx_py_sdk.codec.fx.dex.tx_pb2 import *
from fx_py_sdk.codec.fx.dex.order_pb2 import Direction
from fx_py_sdk.wallet import Address
from fx_py_sdk.constants import *
import logging

DEFAULT_DEX_GAS = 5000000
DEFAULT_GRPC_NONE = "Not found"
DEFAULT_DEC = 1000000000000000000

class GRPCClient:
    def __init__(self, url: str = 'localhost:9090'):
        self.channel = grpc.insecure_channel(url)

    def query_account_info(self, address: str) -> BaseAccount:
        """查询账户信息
            Args:
                address: 账户地址
            Returns:
                account_number：账户number
                sequence：账户nonce
                example:
                    address: "dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy"
                    pub_key {
                      type_url: "/cosmos.crypto.secp256k1.PubKey"
                      value: "\n!\003S\233R\013\216z\2708qK\3312\330\233\340\231\3023+3\271\344!du\014\210\0039\223\245\314"
                    }
                    account_number: 11
                    sequence: 642626
        """
        try:
            # Any 类型转换 - BaseAccount
            account_any = AuthQuery(self.channel).Account(QueryAccountRequest(address=address)).account
            account = BaseAccount()
            if account_any.Is(account.DESCRIPTOR):
                account_any.Unpack(account)
                return account
        except:
            return None

    def query_all_balances(self, address: str) -> []:
        """查询所有余额.
            Args:
                address: 账户地址
            Returns:
                example:
                    {'FX': 999000000.0, 'dai': 1000000000.0, 'usdc': 1000000000.0, 'usdt': 1000000000.0}
            """
        response = BankQuery(self.channel).AllBalances(QueryAllBalancesRequest(address=address))
        coins = dict()
        for c in response.balances:
            balance = decimal.Decimal(c.amount)
            balance = balance / decimal.Decimal(DEFAULT_DEC)
            coins[c.denom] = float(str(balance))
        return coins

    def query_balance(self, address: str, denom: str) -> dict:
        """查询Denom对应的余额.
            Args:
                address: 账户地址
                denom: 币种名称
            Returns:
                example:
                    {'FX': 100.0}
        """
        response = BankQuery(self.channel).Balance(QueryBalanceRequest(address=address, denom=denom))
        balance = decimal.Decimal(response.balance.amount)
        balance = balance / decimal.Decimal(DEFAULT_DEC)
        coin = dict()
        coin[denom] = float(str(balance))
        return coin

    def query_gas_price(self) -> [Coin]:
        """查询gas price"""
        response = OtherQuery(self.channel).GasPrice(GasPriceRequest())
        return response.gas_prices

    def query_chain_id(self) -> str:
        """查询 chain id"""
        response = TendermintClient(self.channel).GetLatestBlock(GetBlockByHeightRequest())
        return response.block.header.chain_id

    """fx dex api"""

    # 查询仓位
    #   owner: 仓位持有人
    #   pair_id: 交易对
    def query_positions(self, owner: str, pair_id: str) -> [dict]:
        """查询仓位.
            Args:
                owner: 账户地址
                pair_id: 币种名称
            Returns:
                id	string	仓位ID		
                owner	string	仓位持有者地址
                pair_id	string	交易对
                direction	PosDirection	仓位方向
                entry_price	string	开仓价格
                mark_price	string	标记价格
                liquidation_price	string	强平价格
                base_quantity	string	持仓数量
                margin	string	保证金
                leverage	string	杠杆
                unrealized_pnl	string	未实现盈亏
                margin_rate	string	保证金率
                initial_margin	string	初始保证金
                funding_times	int64	仓位变动时（开仓/加仓）所处的资金费率周期
                example:
                    [Position(Id='1', Owner='dex1ggz598a4506llaglzsmhp3r23hfke6nw29wans', PairId='tsla:usdt', Direction=1, EntryPrice=1000.4, MarkPrice=820.0, LiquidationPrice=1089.5445544554455, BaseQuantity=0.5, Margin=50.02, Leverage=10, UnrealizedPnl=90.2, MarginRate=0.029239766081871343, InitialMargin=50.02, PendingOrderQuantity=0.0)]
            """

        positions = []
        try:
            response = DexQuery(self.channel).QueryPosition(
                QueryPositionReq(owner=Address(owner).to_bytes(), pair_id=pair_id))
            for pos in response.positions:
                entry_price = decimal.Decimal(pos.entry_price)
                entry_price = entry_price / decimal.Decimal(DEFAULT_DEC)
                entry_price = float(str(entry_price))

                mark_price = decimal.Decimal(pos.mark_price)
                mark_price = mark_price / decimal.Decimal(DEFAULT_DEC)
                mark_price = float(str(mark_price))

                liquidation_price = decimal.Decimal(pos.liquidation_price)
                liquidation_price = liquidation_price / decimal.Decimal(DEFAULT_DEC)
                liquidation_price = float(str(liquidation_price))

                base_quantity = decimal.Decimal(pos.base_quantity)
                base_quantity = base_quantity / decimal.Decimal(DEFAULT_DEC)
                base_quantity = float(str(base_quantity))

                margin = decimal.Decimal(pos.margin)
                margin = margin / decimal.Decimal(DEFAULT_DEC)
                margin = float(str(margin))

                unrealized_pnl = decimal.Decimal(pos.unrealized_pnl)
                unrealized_pnl = unrealized_pnl / decimal.Decimal(DEFAULT_DEC)
                unrealized_pnl = float(str(unrealized_pnl))

                margin_rate = decimal.Decimal(pos.margin_rate)
                margin_rate = margin_rate / decimal.Decimal(DEFAULT_DEC)
                margin_rate = float(str(margin_rate))

                initial_margin = decimal.Decimal(pos.initial_margin)
                initial_margin = initial_margin / decimal.Decimal(DEFAULT_DEC)
                initial_margin = float(str(initial_margin))

                pending_order_quantity = decimal.Decimal(pos.pending_order_quantity)
                pending_order_quantity = pending_order_quantity / decimal.Decimal(DEFAULT_DEC)
                pending_order_quantity = float(str(pending_order_quantity))

                position = Position(
                    pos.id,
                    Address(pos.owner).to_string(),
                    pos.pair_id,
                    pos.direction,
                    entry_price,
                    mark_price,
                    liquidation_price,
                    base_quantity,
                    margin,
                    pos.leverage,
                    unrealized_pnl,
                    margin_rate,
                    initial_margin,
                    pending_order_quantity)
                positions.append(position)

        except Exception as e:
            print("query_position: ", e)
            return "not found"

        return positions

    def query_order(self, order_id: str):
        """根据订单ID查询订单.
            Args:
                order_id: 订单id
            Returns:
                tx_hash	string	交易哈希		
                id	string	订单id	
                owner	string	订单拥有者地址	
                pair_id	string	交易对	
                direction	Direction	订单方向	
                price	string	开单价格	
                base_quantity	string	开单数量(挂单数量，成交后减少)	
                quote_quantity	string	开单占用保证金数量	
                filled_quantity	string	订单已成交数量	
                filled_avg_price	string	订单已成交均价	
                remain_locked	string	订单剩余未成交数量
                ttl	int64	到期时间（秒）
                created_at	string	创建时间
                leverage	int64	杠杆
                status	OrderStatus	订单状态
                order_type	OrderType	订单类型
                cost_fee	string ｜消耗费用
                locked_fee	string｜ 锁定费用

                example:
                    Order(TxHash='F6EA065DD58257AE1AB2F22AE45040A1F8E747E5668F3E8DF857CA222B38B85A', Id='ID-706-1', Owner='dex1ggz598a4506llaglzsmhp3r23hfke6nw29wans', PairId='tsla:usdc', Direction=0, Price=1000.4, BaseQuantity=0.5, QuoteQuantity=50.02, FilledQuantity=0.0, FilledAvgPrice=0.0, RemainLocked=500.2, Leverage=10, Status=0, OrderType=0, CostFee=0.0, LockedFee=0.20008, Ttl=86400)
        """
        try:
            response = DexQuery(self.channel).QueryOrder(QueryOrderRequest(order_id=order_id))
            order = response.order
            price = decimal.Decimal(order.price)
            price = price / decimal.Decimal(DEFAULT_DEC)
            price = float(str(price))

            base_quantity = decimal.Decimal(order.base_quantity)
            base_quantity = base_quantity / decimal.Decimal(DEFAULT_DEC)
            base_quantity = float(str(base_quantity))

            quote_quantity = decimal.Decimal(order.quote_quantity)
            quote_quantity = quote_quantity / decimal.Decimal(DEFAULT_DEC)
            quote_quantity = float(str(quote_quantity))

            filled_quantity = decimal.Decimal(order.filled_quantity)
            filled_quantity = filled_quantity / decimal.Decimal(DEFAULT_DEC)
            filled_quantity = float(str(filled_quantity))

            filled_avg_price = decimal.Decimal(order.filled_avg_price)
            filled_avg_price = filled_avg_price / decimal.Decimal(DEFAULT_DEC)
            filled_avg_price = float(str(filled_avg_price))

            remain_locked = decimal.Decimal(order.remain_locked)
            remain_locked = remain_locked / decimal.Decimal(DEFAULT_DEC)
            remain_locked = float(str(remain_locked))

            cost_fee = decimal.Decimal(order.cost_fee)
            cost_fee = cost_fee / decimal.Decimal(DEFAULT_DEC)
            cost_fee = float(str(cost_fee))

            locked_fee = decimal.Decimal(order.locked_fee)
            locked_fee = locked_fee / decimal.Decimal(DEFAULT_DEC)
            locked_fee = float(str(locked_fee))

            print(order.created_at)

            new_order = Order(
                order.tx_hash,
                order.id,
                Address(order.owner).to_string(),
                order.pair_id,
                order.direction,
                price,
                base_quantity,
                quote_quantity,
                filled_quantity,
                filled_avg_price,
                remain_locked,
                order.leverage,
                order.status,
                order.order_type,
                cost_fee,
                locked_fee,
                order.ttl, )
            return new_order

        except Exception as e:
            print("query orders: ", e)
            return "not found"


    def query_orders(self, owner: str, pair_id: str, page=b"1".decode('utf-8'), limit=b"20".decode('utf-8')):
        """根据账户和交易对查询订单.
            Args:
                owner: 仓位持有地址
                pair_id: 交易对
                page:
                limit:
            Returns:
                orders	Orders	订单列表
                example:
            [Order(TxHash='236A2424826BE4C3F75F33B2835E47063F1F7077D8AFC63CFAE73C31A9810BF9', Id='ID-5-1', Owner='dex1ggz598a4506llaglzsmhp3r23hfke6nw29wans', PairId='tsla:usdc', Direction=0, Price=1000.4, BaseQuantity=0.5, QuoteQuantity=50.02, FilledQuantity=0.0, FilledAvgPrice=0.0, RemainLocked=500.2, Leverage=10, Status=0, OrderType=0, CostFee=0.0, LockedFee=0.20008, Ttl=86400),
            Order(TxHash='3F9656C61695AFCE827ADC19D5B2E51CA9B5682E1EC4020DD091E4C9DD1F83FF', Id='ID-7-1', Owner='dex1ggz598a4506llaglzsmhp3r23hfke6nw29wans', PairId='tsla:usdc', Direction=0, Price=1000.4, BaseQuantity=0.5, QuoteQuantity=50.02, FilledQuantity=0.0, FilledAvgPrice=0.0, RemainLocked=500.2, Leverage=10, Status=0, OrderType=0, CostFee=0.0, LockedFee=0.20008, Ttl=86400)]
        """
        orders = []
        try:
            response = DexQuery(self.channel).QueryOrders(QueryOrdersRequest(
                owner=Address(owner).to_bytes(), pair_id=pair_id, page=page, limit=limit))

            for order in response.orders:
                price = decimal.Decimal(order.price)
                price = price / decimal.Decimal(DEFAULT_DEC)
                price = float(str(price))

                base_quantity = decimal.Decimal(order.base_quantity)
                base_quantity = base_quantity / decimal.Decimal(DEFAULT_DEC)
                base_quantity = float(str(base_quantity))

                quote_quantity = decimal.Decimal(order.quote_quantity)
                quote_quantity = quote_quantity / decimal.Decimal(DEFAULT_DEC)
                quote_quantity = float(str(quote_quantity))

                filled_quantity = decimal.Decimal(order.filled_quantity)
                filled_quantity = filled_quantity / decimal.Decimal(DEFAULT_DEC)
                filled_quantity = float(str(filled_quantity))


                filled_avg_price = decimal.Decimal(order.filled_avg_price)
                filled_avg_price = filled_avg_price / decimal.Decimal(DEFAULT_DEC)
                filled_avg_price = float(str(filled_avg_price))

                remain_locked = decimal.Decimal(order.remain_locked)
                remain_locked = remain_locked / decimal.Decimal(DEFAULT_DEC)
                remain_locked = float(str(remain_locked))

                cost_fee = decimal.Decimal(order.cost_fee)
                cost_fee = cost_fee / decimal.Decimal(DEFAULT_DEC)
                cost_fee = float(str(cost_fee))

                locked_fee = decimal.Decimal(order.locked_fee)
                locked_fee = locked_fee / decimal.Decimal(DEFAULT_DEC)
                locked_fee = float(str(locked_fee))

                print(order.created_at)

                new_order = Order(
                    order.tx_hash,
                    order.id,
                    Address(order.owner).to_string(),
                    order.pair_id,
                    order.direction,
                    price,
                    base_quantity,
                    quote_quantity,
                    filled_quantity,
                    filled_avg_price,
                    remain_locked,
                    order.leverage,
                    order.status,
                    order.order_type,
                    cost_fee,
                    locked_fee,
                    order.ttl,)
                orders.append(new_order)

        except Exception as e:
            print("query orders: ", e)
            return "not found"

        return orders

    def query_funding_info(self):
        """查询资金费率.
            Args:
                无需传参
            Returns:
                funding_period：资金费率结算周期
                next_funding_time：下次资金费率结算时间
                funding_times：资金费率结算次数
                next_log_time：下次抛出资金费率日志的时间
                log_funding_period：资金费率日志的时间周期
                max_funding_per_block：最大资金费率结算数量

                example:
                    funding {
                      funding_period: 14400
                      next_funding_time: 1638867900
                      funding_times: 27
                      next_log_time: 1638845352
                      log_funding_period: 300
                      max_funding_per_block: 1000
                    }
        """
        response = DexQuery(self.channel).QueryFunding(QueryFundingReq())
        return response

    def query_funding_rate(self, pair_id, funding_times, query_all):
        """查询资金费率.
            Args:
                pair_id: 交易对
                funding_times: 结算次数
                query_all：是否查询该交易对所有的资金费率
            Returns:
                pair_id: 交易对
                funding_rate：资金费率
                funding_time：资金费率结算时间

                example:
                    pair_funding_rates {
                      pair_id: "tsla:usdt"
                      funding_rate: "100000000000000"
                      funding_time: 1638306300
                    }
        """
        response = DexQuery(self.channel).QueryPairFundingRates(QueryPairFundingRatesReq(pair_id=pair_id, funding_times=funding_times, query_all=query_all))
        return response

    def query_orderbook(self, pair_id):
        """查询资金费率.
            Args:
                pair_id: 交易对
            Returns:
                Asks：卖单
                    price：价格
                    quantity：数量
                Bids：买单
                Asks {
                  price: "1239.740000000000000000"
                  quantity: "0.277000000000000000"
                }
                Bids {
                  price: "0.100000000000000000"
                  quantity: "1000000008.413720000000000000"
                }
        """
        response = DexQuery(self.channel).QeuryOrderbook(QueryOrderbookReq(pair_id=pair_id))
        return response

    # 查询标记价格
    #   pair_id: 交易对
    #   query_all: 否查询全部
    def query_mark_price(self, pair_id: str, query_all: bool):
        """
        查询标记价格.
            Args:
                pair_id: 交易对
                query_all: 否查询全部
            Returns:
                pair_mark_price	[]PairPrice	PairPrice的列表
                pair_id	string		否	btc:usd
                query_all	bool	一般查链上所有的交易对，也可以单独查某一个交易对

                example:
                pair_mark_price {
                      pair_id: "tsla:usdt"
                      price: "1078550000000000000000"
                    }
                    pair_mark_price {
                      pair_id: "aapl:usdt"
                      price: "168065000000000000000"
                    }
        """
        response = DexQuery(self.channel).QueryMarkPrice(QueryMarkPriceReq(pair_id=pair_id, query_all=query_all))
        return response

    def create_order(self, tx_builder: TxBuilder, pair_id: str, direction: Direction, price: float, base_quantity: float, leverage: int,
                     acc_seq: int, mode: BroadcastMode = BROADCAST_MODE_BLOCK):
        """创建订单"""

        price = decimal.Decimal(str(price))
        price = price * decimal.Decimal(DEFAULT_DEC)
        price = str(price)
        price_split = price.split('.', 1)

        base_quantity = decimal.Decimal(str(base_quantity))
        base_quantity = base_quantity * decimal.Decimal(DEFAULT_DEC)
        base_quantity = str(base_quantity)
        base_quantity_split = base_quantity.split('.', 1)

        msg = MsgCreateOrder(owner=tx_builder.acc_address(), pair_id=pair_id, direction=direction, price=price_split[0],
                             base_quantity=base_quantity_split[0],
                             ttl=1000, leverage=leverage)

        msg_any = Any(type_url='/fx.dex.MsgCreateOrder', value=msg.SerializeToString())
        # DEX 交易设置固定gas
        tx = self.build_tx(tx_builder, acc_seq, [msg_any], DEFAULT_DEX_GAS)
        tx_response = self.broadcast_tx(tx, mode)
        return tx_response

    def cancel_order(self, tx_builder: TxBuilder, order_id: str,
                     acc_seq: int, mode: BroadcastMode = BROADCAST_MODE_BLOCK):
        """取消订单"""
        msg = MsgCancelOrder(owner=tx_builder.acc_address(), order_id=order_id)
        msg_any = Any(type_url='/fx.dex.MsgCancelOrder', value=msg.SerializeToString())
        # DEX 交易设置固定gas
        tx = self.build_tx(tx_builder, acc_seq, [msg_any], DEFAULT_DEX_GAS)
        return self.broadcast_tx(tx, mode)

    def close_position(self, tx_builder: TxBuilder, pair_id: str, position_id: str, price: float, base_quantity: float,
                       acc_seq: int, mode: BroadcastMode = BROADCAST_MODE_BLOCK):
        price = decimal.Decimal(str(price))
        price = price * decimal.Decimal(DEFAULT_DEC)
        price = str(price)
        price_split = price.split('.', 1)


        base_quantity = decimal.Decimal(str(base_quantity))
        base_quantity = base_quantity * decimal.Decimal(DEFAULT_DEC)
        base_quantity = str(base_quantity)
        base_quantity_split = base_quantity.split('.', 1)

        msg = MsgClosePosition(owner=tx_builder.acc_address(), pair_id=pair_id, position_id=position_id, price=price_split[0],
                               base_quantity=base_quantity_split[0])

        msg_any = Any(type_url='/fx.dex.MsgClosePosition', value=msg.SerializeToString())
        # DEX 交易设置固定gas
        tx = self.build_tx(tx_builder, acc_seq, [msg_any], DEFAULT_DEX_GAS)
        return self.broadcast_tx(tx, mode)

    def build_tx(self, tx_builder: TxBuilder, acc_seq: int, msg: [Any], gas_limit: int = 0) -> Tx:
        """签名交易"""
        if tx_builder.chain_id == '':
            # 查询chain_id
            tx_builder.chain_id = self.query_chain_id()

        if tx_builder.account_number <= -1:
            # 查询账户信息
            account = self.query_account_info(tx_builder.address())
            tx_builder.account_number = account.account_number

        gas_price_amount = int(tx_builder.gas_price.amount)
        fee_denom = tx_builder.gas_price.denom
        if gas_price_amount <= 0:
            # 如果未设置gas price 查询链上gas price
            for item in self.query_gas_price():
                if item.denom == fee_denom:
                    gas_price_amount = int(item.amount)

        if gas_limit <= 0:
            # 计算默认的gas amount
            fee_amount = Coin(amount=str(gas_limit * gas_price_amount), denom=fee_denom)
            fee = Fee(amount=[fee_amount], gas_limit=gas_limit)
            tx = tx_builder.sign(acc_seq, msg, fee)
            # 估算gas limit
            gas_info = self.estimating_gas(tx)
            gas_limit = int(float(gas_info.gas_used) * 1.5)

        fee_amount = Coin(amount=str(gas_limit * gas_price_amount), denom=fee_denom)
        fee = Fee(amount=[fee_amount], gas_limit=gas_limit)
        return tx_builder.sign(acc_seq, msg, fee)

    def estimating_gas(self, tx: Tx) -> GasInfo:
        """估算交易Gas limit"""
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