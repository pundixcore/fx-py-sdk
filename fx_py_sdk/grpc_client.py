import decimal
import string
import time
import datetime
import re
from urllib.parse import urlparse

import eth_utils
import grpc
from fx_py_sdk.codec.cosmos.auth.v1beta1.auth_pb2 import BaseAccount
from fx_py_sdk.codec.cosmos.base.query.v1beta1.pagination_pb2 import PageRequest
from fx_py_sdk.codec.cosmos.auth.v1beta1.query_pb2 import QueryAccountRequest, QueryAccountsRequest
from fx_py_sdk.codec.cosmos.auth.v1beta1.query_pb2_grpc import QueryStub as AuthQuery
from fx_py_sdk.codec.cosmos.bank.v1beta1.query_pb2 import QueryAllBalancesRequest, QueryBalanceRequest
from fx_py_sdk.codec.cosmos.bank.v1beta1.query_pb2_grpc import QueryStub as BankQuery
from fx_py_sdk.codec.cosmos.base.tendermint.v1beta1.query_pb2 import GetBlockByHeightRequest
from fx_py_sdk.codec.cosmos.base.tendermint.v1beta1.query_pb2_grpc import ServiceStub as TendermintClient
from fx_py_sdk.codec.cosmos.base.abci.v1beta1.abci_pb2 import GasInfo
from fx_py_sdk.codec.cosmos.base.abci.v1beta1.abci_pb2 import TxResponse
from fx_py_sdk.codec.cosmos.tx.v1beta1.service_pb2_grpc import ServiceStub as TxClient
from fx_py_sdk.codec.cosmos.tx.v1beta1.service_pb2 import (
    SimulateRequest, BroadcastTxRequest, GetTxRequest, BroadcastMode, BROADCAST_MODE_BLOCK, BROADCAST_MODE_SYNC
)

from fx_py_sdk.codec.cosmos.tx.v1beta1.tx_pb2 import Tx, TxRaw, Fee
from fx_py_sdk.codec.cosmos.base.v1beta1.coin_pb2 import Coin
from fx_py_sdk.codec.fx.other.query_pb2 import GasPriceRequest
from fx_py_sdk.codec.fx.other.query_pb2_grpc import QueryStub as OtherQuery
from google.protobuf.any_pb2 import Any
from fx_py_sdk.builder import TxBuilder

from fx_py_sdk.codec.fx.dex.v1.query_pb2_grpc import QueryStub as DexQuery
from fx_py_sdk.codec.fx.dex.v1.query_pb2 import *
from fx_py_sdk.codec.fx.dex.v1.tx_pb2 import *
from fx_py_sdk.codec.fx.dex.v1.order_pb2 import Direction

from fx_py_sdk.codec.fx.oracle.v1.query_pb2_grpc import QueryStub as OracleQuery
from fx_py_sdk.codec.fx.oracle.v1.query_pb2 import QueryPriceRequest
from fx_py_sdk.codec.fx.ibc.applications.transfer.v1.tx_pb2 import *
from fx_py_sdk.codec.ibc.core.client.v1.client_pb2 import Height

from fx_py_sdk.constants import *
from google.protobuf.json_format import MessageToJson
import json
import requests
from fx_py_sdk.model.crud import Crud
from fx_py_sdk.model.model import HedgingOrder, HedgingTrade, Order as CrudOrder, Trade as CrudTrade, Block
from fx_py_sdk.codec.cosmos.gov.v1beta1.query_pb2_grpc import QueryStub as GovQuery
from fx_py_sdk.codec.cosmos.gov.v1beta1.query_pb2 import *

DEFAULT_DEX_GAS = 50000000
DEFAULT_GRPC_NONE = "Not found"
DEFAULT_DEC = 1000000
DEFAULT_DEC_FX = 1000000000000000000
Address_Prefix = "0x"

class GRPCClient:
    def __init__(self, url: str = 'localhost:9090'):
        if urlparse(url).scheme == "https":
            self.channel = grpc.secure_channel(
                urlparse(url).netloc, grpc.ssl_channel_credentials())
        else:
            self.channel = grpc.insecure_channel(url)

        self.crud = Crud()

    def Proposal(self, proposal_id):
        response = GovQuery(self.channel).Proposal(QueryProposalRequest(proposal_id=proposal_id))
        return response


    def query_accounts(self, key: bytes):
        resp = AuthQuery(self.channel).Accounts(QueryAccountsRequest(pagination=PageRequest(
            key=key,
            limit=100,
        )))
        return resp


    def query_account_info(self, address: str) -> BaseAccount:
        """??????????????????
            Args:
                address: ????????????
            Returns:
                account_number?????????number
                sequence?????????nonce
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
            # Any ???????????? - BaseAccount
            account_any = AuthQuery(self.channel).Account(QueryAccountRequest(address=address)).account
            account = BaseAccount()
            if account_any.Is(account.DESCRIPTOR):
                account_any.Unpack(account)
                return account
        except:
            return None

    def query_all_balances(self, address: str) -> []:
        """??????????????????.
            Args:
                address: ????????????
            Returns:
                example:
                    {'FX': 999000000.0, 'dai': 1000000000.0, 'usdc': 1000000000.0, 'usdt': 1000000000.0}
            """
        response = BankQuery(self.channel).AllBalances(
            QueryAllBalancesRequest(address=address))
        coins = dict()
        for c in response.balances:
            balance = decimal.Decimal(c.amount)
            balance = balance / decimal.Decimal(DEFAULT_DEC)
            coins[c.denom] = float(str(balance))
        return coins

    def query_balance(self, address: str, denom: str) -> dict:
        """??????Denom???????????????.
            Args:
                address: ????????????
                denom: ????????????
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
        """??????gas price"""
        response = OtherQuery(self.channel).GasPrice(GasPriceRequest())
        return response.gas_prices

    def query_chain_id(self) -> str:
        """?????? chain id"""
        response = TendermintClient(self.channel).GetLatestBlock(
            GetBlockByHeightRequest())
        return response.block.header.chain_id

    def get_latest_block(self) -> str:
        """?????? latest block"""
        response = TendermintClient(self.channel).GetLatestBlock(
            GetBlockByHeightRequest())
        return response.block.header

    def query_orders_by_account(self, address: str, page_index: int, page_size: int) -> []:
        """???????????????????????????
        args:
            address:???????????????
            page_index?????????
            page_size???????????????
        """

        orders = []
        try:
            r = requests.post(url=BackEndApi.query_order_page, data=json.dumps({'address': address,
                                                                                'pageIndex': page_index,
                                                                                'pageSize': page_size}),
                              headers={'Content-Type': 'application/json'})

            data = json.loads(r.text)

            for order in data['data']['data']:
                base_quantity = decimal.Decimal(order['baseQuantity'])
                price = decimal.Decimal(order['price'])
                quote_quantity = decimal.Decimal(order['quoteQuantity'])
                filled_quantity = decimal.Decimal(order['filledQuantity'])
                filled_avg_price = decimal.Decimal(order['filledAvgPrice'])
                cost_fee = decimal.Decimal(order['costFee'])
                locked_fee = decimal.Decimal(order['lockedFee'])

                new_order = Order(
                    order['orderId'],
                    order['ownerAddress'],
                    order['pair'],
                    order['directionName'],
                    price,
                    base_quantity,
                    quote_quantity,
                    filled_quantity,
                    filled_avg_price,
                    order['leverage'],
                    order['statusName'],
                    order['orderTypeName'],
                    cost_fee,
                    locked_fee)

                orders.append(new_order)

        except Exception as e:
            return []

        return orders

    def query_oracle_price(self, pair_id: str) -> Decimal:
        """?????????????????????
            Args:
                pair_id:?????????
            Returns:
                price
                example:
                    919.8
        """
        try:
            response = OracleQuery(self.channel).GetCurrentPrice(
                QueryPriceRequest(pair_id=pair_id))
            price = decimal.Decimal(response.currentPrice.price)
            price = price / decimal.Decimal(DEFAULT_DEC)
            return price
        except Exception as e:
            return Decimal(0)

    def query_positions(self, owner: str, pair_id: str) -> []:
        """????????????.
            Args:
                owner: ????????????
                pair_id: ?????????
            Returns:
                id	string	??????ID		
                owner	string	?????????????????????
                pair_id	string	?????????
                direction	PosDirection	????????????
                entry_price	string	????????????
                mark_price	string	????????????
                liquidation_price	string	????????????
                base_quantity	string	????????????
                margin	string	?????????
                leverage	string	??????
                unrealized_pnl	string	???????????????
                margin_rate	string	????????????
                initial_margin	string	???????????????
                funding_times	int64	????????????????????????/????????????????????????????????????
                example:
                    [Position(Id='961', Owner='dex179q82e7fcck4ftfvf4vfpwkg86jmxf7upext3v', PairId='tsla:usdt', Direction=1, EntryPrice=Decimal('1140.282785843766290421'), MarkPrice=Decimal('1118.254987012654667678'), LiquidationPrice=Decimal('1241.892142998161337064'), BaseQuantity=Decimal('0.00999999999999993'), Margin=Decimal('1.140282785843758246'), Leverage=10, UnrealizedPnl=Decimal('0.220277988311114685'), MarginRate=Decimal('0.082190741365982938'), InitialMargin=Decimal('146.18425314517057959'), PendingOrderQuantity=Decimal('0'))]
            """

        positions = []
        try:
            response = DexQuery(self.channel).QueryPosition(QueryPositionReq(owner=owner, pair_id=pair_id))
            for pos in response.positions:
                entry_price = decimal.Decimal(pos.entry_price)
                entry_price = entry_price / decimal.Decimal(DEFAULT_DEC)

                mark_price = decimal.Decimal(pos.mark_price)
                mark_price = mark_price / decimal.Decimal(DEFAULT_DEC)

                liquidation_price = decimal.Decimal(pos.liquidation_price)
                liquidation_price = liquidation_price / \
                    decimal.Decimal(DEFAULT_DEC)

                base_quantity = decimal.Decimal(pos.base_quantity)
                base_quantity = base_quantity / decimal.Decimal(DEFAULT_DEC)

                margin = decimal.Decimal(pos.margin)
                margin = margin / decimal.Decimal(DEFAULT_DEC)

                unrealized_pnl = decimal.Decimal(pos.unrealized_pnl)
                unrealized_pnl = unrealized_pnl / decimal.Decimal(DEFAULT_DEC)

                margin_rate = decimal.Decimal(pos.margin_rate)
                margin_rate = margin_rate / decimal.Decimal(DEFAULT_DEC)

                initial_margin = decimal.Decimal(pos.initial_margin)
                initial_margin = initial_margin / decimal.Decimal(DEFAULT_DEC)

                pending_order_quantity = decimal.Decimal(
                    pos.pending_order_quantity)
                pending_order_quantity = pending_order_quantity / \
                    decimal.Decimal(DEFAULT_DEC)

                pos_direction = ""
                if str(pos.direction) == '1':
                    pos_direction = "long"
                elif str(pos.direction) == '2':
                    pos_direction = "short"

                checksumAddr = eth_utils.to_checksum_address(Address_Prefix + pos.owner.hex())
                position = Position(
                    pos.id,
                    checksumAddr,
                    pos.pair_id,
                    pos_direction,
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
            return []

        return positions

    # include_trades only works if use_db=True
    def query_order(self, order_id: str, use_db: bool = False, include_trades: bool = False):
        """????????????ID????????????.
            Args:
                order_id: ??????id
            Returns:
                tx_hash	string	????????????		
                id	string	??????id	
                owner	string	?????????????????????	
                pair_id	string	?????????	
                direction	Direction	????????????	
                price	string	????????????	
                base_quantity	string	????????????(??????????????????????????????)	
                quote_quantity	string	???????????????????????????	
                filled_quantity	string	?????????????????????	
                filled_avg_price	string	?????????????????????	
                created_at	string	????????????
                leverage	int64	??????
                status	OrderStatus	????????????
                order_type	OrderType	????????????
                cost_fee	string ???????????????
                locked_fee	string??? ????????????

                example:
                    Order(Id='ID-706-1', Owner='dex1ggz598a4506llaglzsmhp3r23hfke6nw29wans', PairId='tsla:usdc', Direction=0, Price=1000.4, BaseQuantity=0.5, QuoteQuantity=50.02, FilledQuantity=0.0, FilledAvgPrice=0.0, Leverage=10, Status=0, OrderType=0, CostFee=0.0, LockedFee=0.20008)
        """
        if not use_db:
            response = DexQuery(self.channel).QueryOrder(QueryOrderRequest(order_id=order_id))
            order = response.order
            price = decimal.Decimal(order.price)
            price = price / decimal.Decimal(DEFAULT_DEC)

            base_quantity = decimal.Decimal(order.base_quantity)
            base_quantity = base_quantity / decimal.Decimal(DEFAULT_DEC)

            quote_quantity = decimal.Decimal(order.quote_quantity)
            quote_quantity = quote_quantity / decimal.Decimal(DEFAULT_DEC)

            filled_quantity = decimal.Decimal(order.filled_quantity)
            filled_quantity = filled_quantity / decimal.Decimal(DEFAULT_DEC)

            filled_avg_price = decimal.Decimal(order.filled_avg_price)
            filled_avg_price = filled_avg_price / decimal.Decimal(DEFAULT_DEC)

            locked_fee_amount = ''.join(re.split(r'[^0-9]', order.locked_fee))
            cost_fee_amount = ''.join(re.split(r'[^0-9]', order.cost_fee))

            fee_denom = ''.join(re.split(r'[^A-Za-z]', order.locked_fee))
            if fee_denom == '':
                fee_denom = ''.join(re.split(r'[^A-Za-z]', order.cost_fee))

            cost_fee = decimal.Decimal(cost_fee_amount) / decimal.Decimal(DEFAULT_DEC)
            locked_fee = decimal.Decimal(locked_fee_amount) / decimal.Decimal(DEFAULT_DEC)
            checksumAddr = eth_utils.to_checksum_address(Address_Prefix + order.owner.hex())

            new_order = Order(
                order.id,
                checksumAddr,
                order.pair_id,
                order.direction,
                price,
                base_quantity,
                quote_quantity,
                filled_quantity,
                filled_avg_price,
                order.leverage,
                order.status,
                order.order_type,
                cost_fee,
                locked_fee,
                fee_denom,
            )

        else:
            response = (self.crud.session.query(CrudOrder, Block.time)
                            .join(CrudOrder, CrudOrder.block_height==Block.height)
                            .filter(CrudOrder.order_id==order_id)
                            .one())
            trades = self.query_trades(order_id) if include_trades else None

            order = response.Order
            new_order = Order(
                order.order_id,
                order.owner,
                order.pair_id,
                order.direction,
                order.price,
                order.base_quantity,
                order.quote_quantity,
                order.filled_quantity,
                order.filled_avg_price,
                order.leverage,
                order.status,
                order.order_type,
                order.cost_fee,
                order.locked_fee,
                order.fee_denom,
                order.last_filled_quantity,
                response.time,
                trades
            )

        return new_order

    def query_tx(self, tx_hash: str):
        """Queries Tx from chain"""
        return TxClient(self.channel).GetTx(GetTxRequest(hash=tx_hash))

    def query_trades(self, order_id):
        """Queries trades from database given an order ID, sorted by time."""
        response = (self.crud.session.query(CrudTrade.deal_price, CrudTrade.matched_quantity, Block.time)
                           .join(Block, CrudTrade.block_height==Block.height)
                           .filter(CrudTrade.order_id==order_id)
                           .order_by(CrudTrade.block_height)
                           .all())

        trades = []
        for trade in response:
            new_trade = Trade(trade.deal_price, trade.matched_quantity, trade.time)
            trades.append(new_trade)

        return trades

    # include_trades only works if use_db=True
    def query_orders(self, owner: str, pair_id: str, page=b"1".decode('utf-8'), limit=b"20".decode('utf-8'), use_db=False, include_trades=False):
        """????????????????????????????????????.
            Args:
                owner: ??????????????????
                pair_id: ?????????
                page:
                limit:
            Returns:
                orders	Orders	????????????
                example:
            [Order(Id='ID-5-1', Owner='dex1ggz598a4506llaglzsmhp3r23hfke6nw29wans', PairId='tsla:usdc', Direction=0, Price=1000.4, BaseQuantity=0.5, QuoteQuantity=50.02, FilledQuantity=0.0, FilledAvgPrice=0.0, Leverage=10, Status=0, OrderType=0, CostFee=0.0, LockedFee=0.20008),
            Order(Id='ID-7-1', Owner='dex1ggz598a4506llaglzsmhp3r23hfke6nw29wans', PairId='tsla:usdc', Direction=0, Price=1000.4, BaseQuantity=0.5, QuoteQuantity=50.02, FilledQuantity=0.0, FilledAvgPrice=0.0, Leverage=10, Status=0, OrderType=0, CostFee=0.0, LockedFee=0.20008)]
        """

        orders = []

        if not use_db:
            response = DexQuery(self.channel).QueryOrders(QueryOrdersRequest(
                owner=owner, pair_id=pair_id, page=page, limit=limit))

            for order in response.orders:
                price = decimal.Decimal(order.price)
                price = price / decimal.Decimal(DEFAULT_DEC)

                base_quantity = decimal.Decimal(order.base_quantity)
                base_quantity = base_quantity / decimal.Decimal(DEFAULT_DEC)

                quote_quantity = decimal.Decimal(order.quote_quantity)
                quote_quantity = quote_quantity / decimal.Decimal(DEFAULT_DEC)

                filled_quantity = decimal.Decimal(order.filled_quantity)
                filled_quantity = filled_quantity / \
                    decimal.Decimal(DEFAULT_DEC)

                filled_avg_price = decimal.Decimal(order.filled_avg_price)
                filled_avg_price = filled_avg_price / \
                    decimal.Decimal(DEFAULT_DEC)

                locked_fee_amount = ''.join(re.split(r'[^0-9]', order.locked_fee))
                cost_fee_amount = ''.join(re.split(r'[^0-9]', order.cost_fee))

                fee_denom = ''.join(re.split(r'[^A-Za-z]', order.locked_fee))
                if fee_denom == '':
                    fee_denom = ''.join(re.split(r'[^A-Za-z]', order.cost_fee))

                cost_fee = decimal.Decimal(cost_fee_amount) / decimal.Decimal(DEFAULT_DEC)
                locked_fee = decimal.Decimal(locked_fee_amount) / decimal.Decimal(DEFAULT_DEC)
                checksumAddr = eth_utils.to_checksum_address(Address_Prefix + order.owner.hex())

                new_order = Order(
                    order.id,
                    checksumAddr,
                    order.pair_id,
                    order.direction,
                    price,
                    base_quantity,
                    quote_quantity,
                    filled_quantity,
                    filled_avg_price,
                    order.leverage,
                    order.status,
                    order.order_type,
                    cost_fee,
                    locked_fee,
                    fee_denom,
                )
                orders.append(new_order)

        else:

            # if 'orders not found' in e.details():
            #     logging.warn('No orders found in GRPC - returning empty list')
            #     return []

            sql_orders = (self.crud.session.query(CrudOrder, Block.time)
                                           .join(CrudOrder, CrudOrder.block_height==Block.height)
                                           .filter(CrudOrder.owner == owner, CrudOrder.pair_id == pair_id)
                                           .limit(int(limit))
                                           .offset(int(page))
                                           .all())

            if include_trades:
                order_trades = { res.Order.order_id: [] for res in sql_orders }
                order_ids = order_trades.keys()

                sql_trades = (self.crud.session.query(CrudTrade.order_id, CrudTrade.deal_price, CrudTrade.matched_quantity, Block.time)
                                  .join(Block, CrudTrade.block_height==Block.height)
                                  .filter(CrudTrade.order_id.in_(order_ids))
                                  .order_by(CrudTrade.block_height)
                                  .all())

                for response in sql_trades:
                    trade = Trade(response.deal_price, response.matched_quantity, response.time)
                    order_trades[response.order_id].append(trade)

            for response in sql_orders:
                order: CrudOrder = response.Order
                new_order = Order(
                    # order.tx_hash,
                    order.order_id,
                    order.owner,
                    order.pair_id,
                    order.direction,
                    decimal.Decimal(order.price),
                    decimal.Decimal(order.base_quantity),
                    decimal.Decimal(order.quote_quantity),
                    decimal.Decimal(order.filled_quantity),
                    decimal.Decimal(order.filled_avg_price),
                    order.leverage,
                    order.status,
                    order.order_type,
                    decimal.Decimal(order.cost_fee),
                    decimal.Decimal(order.locked_fee),
                    order.fee_denom,
                    decimal.Decimal(order.last_filled_quantity),
                    response.time,
                    order_trades[order.order_id] if include_trades else None
                )

                orders.append(new_order)

        return orders

    def query_open_order_count(self, client_address=None, pair_id=None):
        """Gets count of open orders from database"""
        return self.crud.query_open_order_count(client_address, pair_id)

    def query_open_order_lock_deposit(self, client_address=None, pair_id=None):
        """
        Gets total locked deposit (including margin and locked fee) of open orders.
        """
        return self.crud.query_open_order_lock_deposit(client_address, pair_id)

    def get_contract_exposure(self, address=None, pair_id=None, is_bot=True):
        """Current long-short exposure. Returns a single value if pair_id is provided; otherwise returns dictionary."""
        return self.crud.get_contract_exposure(address, pair_id, is_bot)
    
    def get_dollar_exposure(self, address=None, pair_id=None, is_bot=True):
        """Current long-short exposure * mark price. Returns a single value if pair_id is provided; otherwise returns dictionary."""
        return self.crud.get_dollar_exposure(address, pair_id, is_bot)

    def query_funding_info(self):
        """??????????????????.
            Args:
                ????????????
            Returns:
                funding_period???????????????????????????
                next_funding_time?????????????????????????????????
                funding_times???????????????????????????
                next_log_time??????????????????????????????????????????
                log_funding_period????????????????????????????????????
                max_funding_per_block?????????????????????????????????

                example:
                    {'funding': {'fundingPeriod': '14400', 'nextFundingTime': '1639472700', 'fundingTimes': '4', 'nextLogTime': '1639466219', 'logFundingPeriod': '300', 'maxFundingPerBlock': '1000'}}
        """
        try:
            response = DexQuery(self.channel).QueryFunding(QueryFundingReq())
            res_str = MessageToJson(response)
            res = json.loads(res_str)
            return res
        except Exception as e:
            print("query error: ", e)
            return e

    def query_funding_rate(self, last_or_realtime: bool = True):
        """??????????????????, fundingRate????????????????????????.
            Args:
                last_or_realtime: if True, returns last (previous funding rate)
                                  if False, returns next funding rate estimate
            Returns:
                pair_id: ?????????
                funding_rate???????????????
                funding_time???????????????????????????

                example:
                    {'pairFundingRates': [{'pairId': 'tsla:usdt', 'fundingRate': '0', 'fundingTime': '1639379542'}, {'pairId': 'tsla:usdt', 'fundingRate': '-0.0001', 'fundingTime': '1639386301'}]}
        """
        try:
            response = DexQuery(self.channel).QueryPairFundingRates(QueryPairFundingRatesReq(
                last_or_realtime=last_or_realtime))
            res_str = MessageToJson(response)
            res = json.loads(res_str)
            for rate in res['pairFundingRates']:
                funding_rate = decimal.Decimal(rate['fundingRate'])
                funding_rate = funding_rate / decimal.Decimal(DEFAULT_DEC)
                rate['fundingRate'] = str(funding_rate)
            return res
        except Exception as e:
            print("query error: ", e)
            return e

    def query_orderbook(self, pair_id):
        """??????????????????.
            Args:
                pair_id: ?????????
            Returns:
                Asks?????????
                    price?????????
                    quantity?????????
                Bids?????????
                {"Asks":[{"price":"1157.170000000000000000","quantity":"0.071999999999999562"},{"price":"1157.240000000000000000","quantity":"0.031000000000000000"}],"Bids":[{"price":"1118.396987012654667678","quantity":"6.699999999999999955"},{"price":"1079.623974025309335355","quantity":"19.995000000000000284"},{"price":"1077.610000000000000000","quantity":"0.404000000000000000"}]}
        """
        try:
            response = DexQuery(self.channel).QueryOrderbook(
                QueryOrderbookReq(pair_id=pair_id))
            res_str = MessageToJson(response)
            res = json.loads(res_str)
            return res
        except Exception as e:
            print("query error: ", e)
            return e

    # def query_funding_rate_log(self, pair_id):
    #     """????????????????????????.
    #         Args:
    #             pair_id: ?????????
    #         Returns:
    #             Asks?????????
    #                 price?????????
    #                 quantity?????????
    #             Bids?????????
    #             {'pairFundingRates': {'pairId': 'tsla:usdt', 'fundingRate': '0.133420164103952947', 'fundingTime': '1639474025'}}
    #     """
    #     try:
    #         response = DexQuery(self.channel).QueryFundingRate(
    #             QueryOrderbookReq(pair_id=pair_id))
    #         res_str = MessageToJson(response)
    #         res = json.loads(res_str)
    #         funding_rate = decimal.Decimal(
    #             res['pairFundingRates']['fundingRate'])
    #         funding_rate = funding_rate / decimal.Decimal(DEFAULT_DEC)
    #         res['pairFundingRates']['fundingRate'] = str(funding_rate)
    #         return res
    #     except Exception as e:
    #         print("query error: ", e)
    #         return e

    def query_funding_payments(self, address: str=None, pair_id: str=None, from_datetime: datetime=None):
        return self.crud.get_funding_transfers(
            address=address,
            pair_id=pair_id,
            from_datetime=from_datetime
        )

    # ??????????????????
    #   pair_id: ?????????
    #   query_all: ???????????????
    def query_mark_price(self, pair_id: str, query_all: bool):
        """
        ??????????????????.
            Args:
                pair_id: ?????????
                query_all: ???????????????
            Returns:
                pair_mark_price	[]PairPrice	PairPrice?????????
                pair_id	string		???	btc:usd
                query_all	bool	????????????????????????????????????????????????????????????????????????

                example:
                {'pairMarkPrice': [{'pairId': 'tsla:usdt', 'price': '1130.67510779198068958'}, {'pairId': 'aapl:usdt', 'price': '169'}, {'pairId': 'tsla:usdc', 'price': '1091.970493546293773044'}, {'pairId': 'aapl:usdc', 'price': '167.97'}, {'pairId': 'tsla:dai', 'price': '678.12218871527777799'}, {'pairId': 'aapl:dai', 'price': '124.753180455902777817'}]}
        """
        try:
            response = DexQuery(self.channel).QueryMarkPrice(
                QueryMarkPriceReq(pair_id=pair_id, query_all=query_all))
            res_str = MessageToJson(response)
            res = json.loads(res_str)
            for rate in res['pairMarkPrice']:
                funding_rate = decimal.Decimal(rate['price'])
                funding_rate = funding_rate / decimal.Decimal(DEFAULT_DEC)
                rate['price'] = str(funding_rate)
            return res
        except Exception as e:
            print("query error: ", e)
            return e

    def create_order(self, tx_builder: TxBuilder, pair_id: str, direction: Direction, price: Decimal, base_quantity: Decimal, leverage: int,
                     acc_seq: int, mode: BroadcastMode = BROADCAST_MODE_BLOCK):
        """????????????"""

        price = price * decimal.Decimal(DEFAULT_DEC)
        price = str(price)
        price_split = price.split('.', 1)
        base_quantity = base_quantity * decimal.Decimal(DEFAULT_DEC)
        base_quantity = str(base_quantity)
        base_quantity_split = base_quantity.split('.', 1)

        msg = MsgCreateOrder(owner=tx_builder.account.address,
                             pair_id=pair_id,
                             direction=direction,
                             price=price_split[0],
                             base_quantity=base_quantity_split[0],
                             leverage=leverage)

        msg_any = Any(type_url='/fx.dex.v1.MsgCreateOrder',
                      value=msg.SerializeToString())
        # DEX ??????????????????gas
        tx = self.build_tx(tx_builder, acc_seq, [msg_any], DEFAULT_DEX_GAS)
        tx_response = self.broadcast_tx(tx, mode)
        return tx_response

    def cancel_order(self, tx_builder: TxBuilder, order_id: str,
                     acc_seq: int, mode: BroadcastMode = BROADCAST_MODE_BLOCK):

        """????????????"""
        msg = MsgCancelOrder(owner=tx_builder.account.address, order_id=order_id)
        msg_any = Any(type_url='/fx.dex.v1.MsgCancelOrder',
                      value=msg.SerializeToString())
        # DEX ??????????????????gas
        tx = self.build_tx(tx_builder, acc_seq, [msg_any], DEFAULT_DEX_GAS)
        return self.broadcast_tx(tx, mode)

    def close_position(self, tx_builder: TxBuilder, pair_id: str, position_id: str, price: Decimal, base_quantity: Decimal,
                       full_close: bool, acc_seq: int, market_close=False, mode: BroadcastMode = BROADCAST_MODE_BLOCK):

        price = price * decimal.Decimal(DEFAULT_DEC)
        price = str(price)
        price_split = price.split('.', 1)
        base_quantity = base_quantity * decimal.Decimal(DEFAULT_DEC)
        base_quantity = str(base_quantity)
        base_quantity_split = base_quantity.split('.', 1)

        msg = MsgClosePosition(owner=tx_builder.account.address,
                               pair_id=pair_id,
                               position_id=position_id,
                               price=price_split[0],
                               base_quantity=base_quantity_split[0],
                               full_close=full_close,
                               market_close=market_close)

        msg_any = Any(type_url='/fx.dex.v1.MsgClosePosition',
                      value=msg.SerializeToString())
        # DEX ??????????????????gas
        tx = self.build_tx(tx_builder, acc_seq, [msg_any], DEFAULT_DEX_GAS)
        return self.broadcast_tx(tx, mode)

    def add_margin(self, tx_builder: TxBuilder, pair_id: str, position_id: str, margin: Decimal,
                       acc_seq: int, mode: BroadcastMode = BROADCAST_MODE_BLOCK):

        amount = margin * decimal.Decimal(DEFAULT_DEC)
        amount = str(amount)
        amount_split = amount.split('.', 1)

        msg = MsgAddMargin(owner=tx_builder.account.address, pair_id=pair_id,
                           position_id=position_id, margin=amount_split[0])

        msg_any = Any(type_url='/fx.dex.v1.MsgAddMargin',
                      value=msg.SerializeToString())
        # DEX ??????????????????gas
        tx = self.build_tx(tx_builder, acc_seq, [msg_any], DEFAULT_DEX_GAS)
        return self.broadcast_tx(tx, mode)


    def ibc_transfer(self, tx_builder: TxBuilder, channel: str, token_amount: int, receiver: str, denom: str,
                       acc_seq: int, mode: BroadcastMode = BROADCAST_MODE_BLOCK):
        if tx_builder._private_key is not None:
            address = tx_builder._private_key.to_address()
            if denom == "USDT":
                amount = token_amount * decimal.Decimal(DEFAULT_DEC)
            else:
                amount = token_amount * decimal.Decimal(DEFAULT_DEC_FX)
        else:
            address = tx_builder.account.address
            amount = token_amount * decimal.Decimal(DEFAULT_DEC)
        amount = str(amount)
        amount_split = amount.split('.', 1)
        token = Coin(amount=str(amount_split[0]), denom=denom)

        height = Height(revision_number=0, revision_height=0)
        dtime = datetime.datetime.now()
        ans_time = time.mktime(dtime.timetuple())
        ans_time = (int(ans_time) + 86400) * 1000 * 1000 * 1000

        msg = MsgTransfer(source_port="transfer",
                          source_channel=channel,
                          token=token,
                          sender=address,
                          receiver=receiver,
                          timeout_height=height,
                          timeout_timestamp=ans_time,
                          router="",
                          fee=Coin(amount=str(0), denom=denom))

        msg_any = Any(type_url='/fx.ibc.applications.transfer.v1.MsgTransfer',
                      value=msg.SerializeToString())
        tx = self.build_tx(tx_builder, acc_seq, [msg_any], DEFAULT_DEX_GAS)
        return self.broadcast_tx(tx, mode)

    def build_tx(self, tx_builder: TxBuilder, acc_seq: int, msg: [Any], gas_limit: int = 0) -> Tx:
        """????????????"""
        if tx_builder.chain_id == '':
            # ??????chain_id
            tx_builder.chain_id = self.query_chain_id()

        account = self.query_account_info(tx_builder.address())
        tx_builder.account_number = account.account_number

        gas_price_amount = int(tx_builder.gas_price.amount) / DEFAULT_DEC
        fee_denom = tx_builder.gas_price.denom
        if gas_price_amount <= 0:
            # ???????????????gas price ????????????gas price
            for item in self.query_gas_price():
                if item.denom == fee_denom:
                    gas_price_amount = int(item.amount)

        if gas_limit <= 0:
            # ???????????????gas amount
            fee_amount = Coin(amount=str(
                round(gas_limit * gas_price_amount)), denom=fee_denom)
            fee = Fee(amount=[fee_amount], gas_limit=gas_limit)
            tx = tx_builder.sign(acc_seq, msg, fee)
            # ??????gas limit
            gas_info = self.estimating_gas(tx)
            gas_limit = int(float(gas_info.gas_used) * 1.5)

        fee_amount = Coin(amount=str(
            round(gas_limit * gas_price_amount)), denom=fee_denom)
        fee = Fee(amount=[fee_amount], gas_limit=gas_limit)
        return tx_builder.sign(acc_seq, msg, fee)

    def estimating_gas(self, tx: Tx) -> GasInfo:
        """????????????Gas limit"""
        response = TxClient(self.channel).Simulate(SimulateRequest(tx=tx))
        return response.gas_info

    def broadcast_tx(self, tx: Tx, mode: BroadcastMode = BROADCAST_MODE_BLOCK) -> TxResponse:
        """????????????"""
        tx_raw = TxRaw(body_bytes=tx.body.SerializeToString(),
                       auth_info_bytes=tx.auth_info.SerializeToString(),
                       signatures=tx.signatures)
        tx_bytes = tx_raw.SerializeToString()
        response = TxClient(self.channel).BroadcastTx(
            BroadcastTxRequest(tx_bytes=tx_bytes, mode=mode))
        return response.tx_response

    ### Database insertion functions ###
    def insert_hedging_order(self, order: HedgingOrder):
        """Inserts hedging order into database"""
        self.crud.insert(order)

    def insert_hedging_trade(self, trade: HedgingTrade):
        """Inserts hedging trade into database"""
        self.crud.insert(trade)
    
    def insert_hedging_trades(self, trades: Iterable[HedgingTrade]):
        """Inserts multiple hedging trades into database"""
        self.crud.insert_many(trades)

    def query_funding_transfers(self, address: str = None, pair_id: str = None, from_ts: float = None):
        """Queries funding transfers from database.
            Args:
                address: owner of positions of these funding transfers
                pair_id: related pair_id
                from_ts: timestamp to query from
            Returns:

        """
        self.crud
