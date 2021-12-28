from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from fx_py_sdk.model.model import *
from sqlalchemy import or_


class Crud:
    def __init__(self):
        sql = Sql("fxdex")
        self.DBSession = sessionmaker(bind=sql.engine)
        self.session=self.DBSession()

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

    def get_positions(self, address: str):
        return self.session.query(Position).filter(Position.owner == address)

    def get_orders_by_owner(self, owner: str) -> []:
        return self.session.query(Order).filter(Order.owner == owner)

    def get_orderbook_from_orderbook(self, pair_id: str):
        """get orderbook from sql orderbook table"""
        orderbook_ask = self.session.query(Orderbook.price, Orderbook.quantity).filter(Orderbook.pair_id == pair_id,
                                             Orderbook.direction == 'ASK').\
            order_by(Orderbook.price).limit(100)

        orderbook_bid = self.session.query(Orderbook.price, Orderbook.quantity).filter(Orderbook.pair_id == pair_id,
                                             Orderbook.direction == 'BID'). \
            order_by(Orderbook.price.desc()).limit(100)
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