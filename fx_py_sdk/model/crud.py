from decimal import Decimal
from typing import Dict, Iterable, List, Union
from sqlalchemy.orm import sessionmaker
from sqlalchemy import case, create_engine
from sqlalchemy.orm.session import Session
from fx_py_sdk.codec.fx.dex.match_pb2 import OrderBook
from fx_py_sdk.model.model import *
from sqlalchemy import or_, and_, func

class Crud:
    def __init__(self):
        sql = Sql("fxdex")
        self.DBSession = sessionmaker(bind=sql.engine, autocommit=False)
        self.session: Session = self.DBSession()

    def insert(self, object):
        self.session.add(object)
        self.session.commit()

    def insert_many(self, objectlist):
        self.session.add_all(objectlist)
        self.session.commit()

    def filterone(self, object, filter):
        return self.session.query(object).filter(filter).first()

    def filter_many(self, object, filter):
        return self.session.query(object).filter(filter)

    def update(self, object, filter, updic):
        self.session.query(object).filter(filter).update(updic)
        self.session.commit()

    def delete(self, object):
        self.session.delete(object)
        self.session.commit()

    def get_funding_transfer(self, address: str):
        return self.session.query(FundingTransfer).filter(FundingTransfer.owner == address)

    def get_positions(self, address: str):
        return self.session.query(Position).filter(Position.owner == address)

    def get_orders_by_owner(self, owner: str) -> List[Order]:
        return self.session.query(Order).filter(Order.owner == owner)

    def get_latest_orderbook_record(self, price, pair_id, direction):
        return (self.session.query(Orderbook)
                            .filter(and_(Orderbook.price==price, Orderbook.pair_id==pair_id, Orderbook.direction==direction))
                            .order_by(Orderbook.block_height.desc(), Orderbook.id.desc())
                            .first())

    def get_latest_trade(self, order_id):
        return (self.session.query(Trade)
                            .filter(Trade.order_id==order_id)
                            .order_by(Trade.block_height.desc(), Trade.id.desc())
                            .first())

    def get_orderbook_from_orderbook(self, pair_id: str):
        """get orderbook from sql orderbook table"""
        orderbook_ask = self.session.query(Orderbook.price, Orderbook.quantity).filter(Orderbook.pair_id == pair_id,
                                             Orderbook.direction == 'ASK').order_by(Orderbook.price).limit(100)

        orderbook_bid = self.session.query(Orderbook.price, Orderbook.quantity).filter(Orderbook.pair_id == pair_id,
                                             Orderbook.direction == 'BID').order_by(Orderbook.price.desc()).limit(100)
        orderbook = dict()
        asks = []
        bids = []
        for v in orderbook_ask:
            asks.append(dict(zip(v.keys(), v)))
        for v in orderbook_bid:
            bids.append(dict(zip(v.keys(), v)))
        orderbook['asks'] = asks
        orderbook['bids'] = bids
        return orderbook

    def get_orderbook_from_order(self, pair_id: str):
        """get orderbook from sql order table"""
        orderbook = dict()
        asks = []
        bids = []
        ask_items = dict()
        bid_items = dict()
        # ob = dict(ask=[dict(price=0, quantity=0)], bid=[dict(price=0, quantity=0)])
        order_ask = self.session.query(Order.price, Order.base_quantity).filter(Order.pair_id == pair_id,
                                                     Order.direction == 'ASK',
                                                     or_(Order.status == 'ORDER_PENDING',
                                                         Order.status == 'ORDER_PARTIAL_FILLED')).order_by(Order.price)

        for order in order_ask:
            order_dict = dict(zip(order.keys(), order))
            if order_dict['price'] in ask_items:
                ask_items[order_dict['price']] = ask_items[order_dict['price']] + order_dict['base_quantity']
            else:
                ask_items[order_dict['price']] = order_dict['base_quantity']

        for key in ask_items.keys():
            item = {'price':key, 'quantity':ask_items[key]}
            asks.append(item)

        order_bid = self.session.query(Order.price, Order.base_quantity).filter(Order.pair_id == pair_id,
                                                     Order.direction == 'BID',
                                                     or_(Order.status == 'ORDER_PENDING',
                                                         Order.status == 'ORDER_PARTIAL_FILLED')).order_by(Order.price.desc())
        for order in order_bid:
            order_dict = dict(zip(order.keys(), order))
            if order_dict['price'] in bid_items:
                bid_items[order_dict['price']] = bid_items[order_dict['price']] + order_dict['base_quantity']
            else:
                bid_items[order_dict['price']] = order_dict['base_quantity']

        for key in bid_items.keys():
            item = {'price':key, 'quantity':bid_items[key]}
            bids.append(item)

        orderbook['asks'] = asks
        orderbook['bids'] = bids
        return orderbook

    def __get_open_order_conditions(self, client_address=None, pair_id=None):
        conditions = [Order.status.in_(('ORDER_PENDING', 'ORDER_PARTIAL_FILLED'))]
        if client_address:
            conditions.append(Order.owner==client_address)
        if pair_id:
            conditions.append(Order.pair_id==pair_id)
        return conditions        

    def query_open_order_count(self, client_address=None, pair_id=None) -> int:
        conditions = self.__get_open_order_conditions(client_address, pair_id)
        return self.session.query(Order).filter(and_(*conditions)).count()

    def query_all_locked_fees(self) -> Iterable:
        order_conditions = self.__get_open_order_conditions()
        order_conditions.append(Order.order_type=='ORDER_TYPE_OPEN_POSITION')
        locked_fees = (self.session.query(Order.pair_id, Order.owner, Order.direction, func.sum(Order.locked_fee))
                          .filter(and_(*order_conditions))
                          .group_by(Order.pair_id, Order.owner, Order.direction)
                          .all())
        return locked_fees

    def query_open_order_lock_deposit(self, client_address=None, pair_id=None) -> Decimal:
        # Locked fee
        order_conditions = self.__get_open_order_conditions(client_address, pair_id)
        order_conditions.append(Order.order_type=='ORDER_TYPE_OPEN_POSITION')
        locked_fee = (self.session.query(func.sum(Order.locked_fee))
                                  .filter(and_(*order_conditions))
                                  .first())[0]

        # Margin = SUM(Order.base_quantity * Order.price / Order.leverage) + Added Margin
        position_conditions = self.__get_open_position_conditions(client_address, pair_id)
        margin = (self.session.query(func.sum(Position.margin))
                              .filter(and_(*position_conditions))
                              .first())[0]

        return locked_fee + margin

    def __get_position_conditions(self, client_address=None, pair_id=None):
        conditions = [Position.status=='open']
        if client_address:
            conditions.append(Position.owner==client_address)
        if pair_id:
            conditions.append(Position.pair_id==pair_id)
        return conditions        

    def __query_best_price(self, block_height, direction):
        conditions = [Order.block_height<=block_height,
                      Order.direction==direction,
                      Order.status.in_(('ORDER_PENDING', 'ORDER_PARTIAL_FILLED'))]

        if direction=='BID':
            price_order = Order.price.desc()
        else:
            price_order = Order.price.asc()

        query = (self.session.query(Order.pair_id, Order.price, Order.block_height)
                             .order_by(Order.pair_id, price_order)
                             .distinct(Order.pair_id)
                             .filter(*conditions))
        return query

    def query_mark_prices(self):
        query = (self.session.query(Position.pair_id, Position.mark_price)
                             .order_by(Position.pair_id, Position.block_height.desc())
                             .distinct(Position.pair_id))
        return query.all()

    def query_best_bid_ask(self, block_height):
        bid_query = self.__query_best_price(block_height, 'BID').subquery()
        ask_query = self.__query_best_price(block_height, 'ASK').subquery()

        query = self.session.query(
            func.coalesce(bid_query.c.pair_id, ask_query.c.pair_id),
            bid_query.c.price,
            ask_query.c.price,
            case(
                [(bid_query.c.block_height > ask_query.c.block_height, bid_query.c.block_height)],
                else_ = ask_query.c.block_height
            )
        ).join(
            ask_query,
            bid_query.c.pair_id==ask_query.c.pair_id,
            full=True
        )

        return query.all()

    def count(self, object):
        return self.session.query(object).count()

    # Exposure
    def __get_exposure(self, address=None, pair_id=None, is_bot=True, as_dollar_value=False) -> Union[Decimal, Dict[str, Decimal]]:
        # Apply SQL conditions based on parameters
        conditions = [Position.status=='open']

        if address:
            conditions.append(Position.owner==address)
        elif is_bot:
            bot_addresses = self.session.query(Wallet.address)
            conditions.append(Position.owner.in_(bot_addresses))

        if pair_id:
            conditions.append(Position.pair_id==pair_id)

        # Retrieve from DB
        result = (self.session.query(Position.pair_id, func.sum(Position.base_quantity * case([(Position.direction=='LONG', 1)], else_=-1)))
                              .filter(*conditions)
                              .group_by(Position.pair_id)
                              .all())
        result_dict = { trade_pair: exposure for trade_pair, exposure in result }

        # Mark quantities to latest mark prices
        if as_dollar_value and result_dict:
            mark_prices = self.query_mark_prices()  # latest mark prices
            for trade_pair, exposure in result_dict.items():
                for mark_pair, mark_price in mark_prices:
                    if trade_pair==mark_pair:
                        result_dict[trade_pair] = exposure * mark_price
                        break

        if pair_id:
            return result_dict.get(pair_id, Decimal('0'))
        else:
            return result_dict

    def get_contract_exposure(self, address=None, pair_id=None, is_bot=True):
        """Returns a single net contract quantity exposure if pair_id is provided. Otherwise, returns dictionary."""
        return self.__get_exposure(address, pair_id, is_bot)
    
    def get_dollar_exposure(self, address=None, pair_id=None, is_bot=True):
        """Returns a single exposure marked to mark price if pair_id is provided. Otherwise, returns dictionary."""
        return self.__get_exposure(address, pair_id, is_bot, as_dollar_value=True)
