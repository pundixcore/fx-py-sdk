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
from fx.dex.tx_pb2 import *
from fx.dex.order_pb2 import Direction
from wallet import Address

DEFAULT_DEX_GAS = 5000000


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
        response = AuthQuery(self.channel).Account(QueryAccountRequest(address=address))
        # Any 类型转换 - BaseAccount
        base_account = BaseAccount()
        response.account.Unpack(base_account)
        return base_account

    def query_all_balances(self, address: str) -> [Coin]:
        """查询所有余额.
            Args:
                address: 账户地址
            Returns:
                example:
                    [denom: "FX"
                    amount: "999999515355700000000000000"
                    , denom: "dai"
                    amount: "1000000000000000000000000000"
                    , denom: "usdc"
                    amount: "998768279527278811008751747"
                    , denom: "usdt"
                    amount: "999993902005180470907691119"
                    ]
            """
        response = BankQuery(self.channel).AllBalances(QueryAllBalancesRequest(address=address))
        return response.balances

    def query_balance(self, address: str, denom: str) -> Coin:
        """查询Denom对应的余额.
            Args:
                address: 账户地址
                denom: 币种名称
            Returns:
                example:
                    denom: "FX"
                    amount: "999999515355700000000000000"
        """
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

    """fx dex api"""

    # 查询仓位
    #   owner: 仓位持有人
    #   pair_id: 交易对
    def query_positions(self, owner: str, pair_id: str):
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
                    positions {
                      id: "1593"
                      owner: "c\304\347\'1C\224\2206\355\231\237|pwR\004\"\234G"
                      pair_id: "tsla:usdt"
                      entry_price: "718593136493812201276"
                      mark_price: "1070360000000000000000"
                      liquidation_price: "654287123015520432741"
                      base_quantity: "1765981856000000000000"
                      margin: "126149732730850940373112"
                      leverage: 10
                      unrealized_pnl: "621213898493956196275164"
                      margin_rate: "41420143008527607"
                      initial_margin: "126902244089420380373112"
                      pending_order_quantity: "0"
                    }
                    positions {
                      id: "1611"
                      owner: "c\304\347\'1C\224\2206\355\231\237|pwR\004\"\234G"
                      pair_id: "tsla:usdt"
                      direction: SHORT
                      entry_price: "1041326589769199070774"
                      mark_price: "1070360000000000000000"
                      liquidation_price: "1140895666081791810609"
                      base_quantity: "21837997000000000000"
                      margin: "2274048694340000000000"
                      leverage: 10
                      unrealized_pnl: "-634031525520000000035"
                      margin_rate: "57010423825594643"
                      initial_margin: "2274048694340000000000"
                      pending_order_quantity: "0"
                    }
            """
        response = DexQuery(self.channel).QueryPosition(
            QueryPositionReq(owner=Address(owner).to_bytes(), pair_id=pair_id))
        return response.positions

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
                    order {
                      tx_hash: "CCC896186F70C77AF904BC4C713791BFCEFE2691869A05871DB6F0E9076DFCA8"
                      id: "ID-880797-1"
                      owner: "B\005B\237\265\243\365\377\365\037\0247p\304j\215\323l\352n"
                      pair_id: "tsla:usdt"
                      price: "1000400000000000000000"
                      base_quantity: "500000000000000000"
                      quote_quantity: "50020000000000000000"
                      filled_quantity: "0"
                      filled_avg_price: "0"
                      remain_locked: "500200000000000000000"
                      created_at {
                        seconds: 1638844669
                        nanos: 525519069
                      }
                      leverage: 10
                      cost_fee: "0"
                      locked_fee: "200080000000000000"
                      ttl: 86400
                    }
        """
        response = DexQuery(self.channel).QueryOrder(QueryOrderRequest(order_id=order_id))
        return response

    def query_orders(self, owner: str, pair_id: str, page: str = 0, limit: str = 20):
        """根据账户和交易对查询订单.
            Args:
                owner: 仓位持有地址
                pair_id: 交易对
                page:
                limit:
            Returns:
                orders	Orders	订单列表
                example:
                orders {
                      orders {
                        tx_hash: "391588EE5E9128FE7862820314EC156D11EC11104F0B5E4AED274A99D647B36B"
                        id: "ID-806841-1"
                        owner: "c\304\347\'1C\224\2206\355\231\237|pwR\004\"\234G"
                        pair_id: "tsla:usdt"
                        price: "909830000000000000000"
                        base_quantity: "312000000000000000"
                        quote_quantity: "28386696000000000000"
                        filled_quantity: "0"
                        filled_avg_price: "0"
                        remain_locked: "283866960000000000000"
                        created_at {
                          seconds: 1638768292
                          nanos: 99804331
                        }
                        leverage: 10
                        cost_fee: "0"
                        locked_fee: "113546784000000000"
                        ttl: 86400
                      }
                      orders {
                        tx_hash: "7193993BFED78849B90FE21585D9911361989A80C4318D69844C3A3E3BFEDB2C"
                        id: "ID-806848-1"
                        owner: "c\304\347\'1C\224\2206\355\231\237|pwR\004\"\234G"
                        pair_id: "tsla:usdt"
                        price: "924530000000000000000"
                        base_quantity: "442000000000000000"
                        quote_quantity: "40864226000000000000"
                        filled_quantity: "0"
                        filled_avg_price: "0"
                        remain_locked: "408642260000000000000"
                        created_at {
                          seconds: 1638768299
                          nanos: 280541328
                        }
                        leverage: 10
                        cost_fee: "0"
                        locked_fee: "163456904000000000"
                        ttl: 86400
                      }
                  }
        """
        response = DexQuery(self.channel).QueryOrders(QueryOrdersRequest(
            owner=Address(owner).to_bytes(), pair_id=pair_id, page=page, limit=limit))
        return response

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
                  price: "651.318912692282338620"
                  quantity: "1775.077576000000000000"
                }
                Asks {
                  price: "971.054271084337349398"
                  quantity: "1.000000000000000000"
                }
                Asks {
                  price: "1004.760000000000000000"
                  quantity: "0.379000000000000000"
                }
                Asks {
                  price: "1110.170000000000000000"
                  quantity: "0.292000000000000000"
                }
                Asks {
                  price: "1113.010000000000000000"
                  quantity: "0.024000000000000000"
                }
                Asks {
                  price: "1123.240000000000000000"
                  quantity: "0.109000000000000000"
                }
                Asks {
                  price: "1127.860000000000000000"
                  quantity: "0.502000000000000000"
                }
                Asks {
                  price: "1128.850000000000000000"
                  quantity: "0.321000000000000000"
                }
                Asks {
                  price: "1134.630000000000000000"
                  quantity: "0.178000000000000000"
                }
                Asks {
                  price: "1134.800000000000000000"
                  quantity: "0.338000000000000000"
                }
                Asks {
                  price: "1136.560000000000000000"
                  quantity: "0.411000000000000000"
                }
                Asks {
                  price: "1150.900000000000000000"
                  quantity: "0.373000000000000000"
                }
                Asks {
                  price: "1154.660000000000000000"
                  quantity: "0.132000000000000000"
                }
                Asks {
                  price: "1181.250000000000000000"
                  quantity: "0.215000000000000000"
                }
                Asks {
                  price: "1185.150000000000000000"
                  quantity: "0.510000000000000000"
                }
                Asks {
                  price: "1192.840000000000000000"
                  quantity: "0.176000000000000000"
                }
                Asks {
                  price: "1193.070000000000000000"
                  quantity: "0.452000000000000000"
                }
                Asks {
                  price: "1194.450000000000000000"
                  quantity: "0.271000000000000000"
                }
                Asks {
                  price: "1201.000000000000000000"
                  quantity: "0.256000000000000000"
                }
                Asks {
                  price: "1214.290000000000000000"
                  quantity: "0.466000000000000000"
                }
                Asks {
                  price: "1216.100000000000000000"
                  quantity: "0.306000000000000000"
                }
                Asks {
                  price: "1221.560000000000000000"
                  quantity: "0.034000000000000000"
                }
                Asks {
                  price: "1221.660000000000000000"
                  quantity: "0.321000000000000000"
                }
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
                    pair_mark_price {
                      pair_id: "tsla:usdc"
                      price: "981152536500000000000"
                    }
                    pair_mark_price {
                      pair_id: "aapl:usdc"
                      price: "171420000000000000000"
                    }
                    pair_mark_price {
                      pair_id: "tsla:dai"
                      price: "820000000000000000000"
                    }
                    pair_mark_price {
                      pair_id: "aapl:dai"
                      price: "145000000000000000000"
                    }
        """
        response = DexQuery(self.channel).QueryMarkPrice(QueryMarkPriceReq(pair_id=pair_id, query_all=query_all))
        return response

    def create_order(self, tx_builder: TxBuilder, pair_id: str, direction: Direction, price: str, base_quantity: str,
                     leverage: int):
        """创建订单"""
        msg = MsgCreateOrder(owner=tx_builder.acc_address(), pair_id=pair_id, direction=direction, price=price,
                             base_quantity=base_quantity,
                             ttl=1000, leverage=leverage)

        msg_any = Any(type_url='/fx.dex.MsgCreateOrder', value=msg.SerializeToString())
        # DEX 交易设置固定gas
        tx = self.build_tx(tx_builder, [msg_any], DEFAULT_DEX_GAS)
        tx_response = self.broadcast_tx(tx)
        return tx_response

    def cancel_order(self, tx_builder: TxBuilder, order_id: str):
        """取消订单"""
        msg = MsgCancelOrder(owner=tx_builder.acc_address(), order_id=order_id)
        msg_any = Any(type_url='/fx.dex.MsgCancelOrder', value=msg.SerializeToString())
        # DEX 交易设置固定gas
        tx = self.build_tx(tx_builder, [msg_any], DEFAULT_DEX_GAS)
        return self.broadcast_tx(tx)

    def close_position(self, tx_builder: TxBuilder, pair_id: str, position_id: str, price: str, base_quantity: str):
        msg = MsgClosePosition(owner=tx_builder.acc_address(), pair_id=pair_id, position_id=position_id, price=price,
                               base_quantity=base_quantity)
        msg_any = Any(type_url='/fx.dex.MsgClosePosition', value=msg.SerializeToString())
        # DEX 交易设置固定gas
        tx = self.build_tx(tx_builder, [msg_any], DEFAULT_DEX_GAS)
        return self.broadcast_tx(tx)

    def build_tx(self, tx_builder: TxBuilder, msg: [Any], gas_limit: int = 0) -> Tx:
        """签名交易"""
        if tx_builder.chain_id == '':
            # 查询chain_id
            tx_builder.chain_id = self.query_chain_id()

        account = self.query_account_info(tx_builder.address())
        if tx_builder.account_number <= -1:
            # 查询账户信息
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
            tx = tx_builder.sign(account.sequence, msg, fee)
            # 估算gas limit
            gas_info = self.estimating_gas(tx)
            gas_limit = int(float(gas_info.gas_used) * 1.5)

        fee_amount = Coin(amount=str(gas_limit * gas_price_amount), denom=fee_denom)
        fee = Fee(amount=[fee_amount], gas_limit=gas_limit)
        return tx_builder.sign(account.sequence, msg, fee)

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
