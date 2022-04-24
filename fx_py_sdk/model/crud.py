import datetime
from decimal import Decimal
from typing import Dict, Iterable, List, Union
from sqlalchemy.orm import sessionmaker
from sqlalchemy import case, create_engine, text
from sqlalchemy.orm.session import Session
from fx_py_sdk.codec.fx.dex.match_pb2 import OrderBook
from fx_py_sdk.model.model import *
from sqlalchemy import or_, and_, func

class Crud:
    def __init__(self):
        self.init_session()

    def init_session(self):
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
        order_ask = (self.session.query(Order.price, Order.base_quantity)
                                 .filter(Order.pair_id == pair_id,
                                         Order.direction == 'ASK',
                                         or_(Order.status == 'ORDER_PENDING',
                                             Order.status == 'ORDER_PARTIAL_FILLED'))
                                 .order_by(Order.price))

        for order in order_ask:
            order_dict = dict(zip(order.keys(), order))
            if order_dict['price'] in ask_items:
                ask_items[order_dict['price']] = ask_items[order_dict['price']] + order_dict['base_quantity']
            else:
                ask_items[order_dict['price']] = order_dict['base_quantity']

        for key in ask_items.keys():
            item = {'price':key, 'quantity':ask_items[key]}
            asks.append(item)

        order_bid = (self.session.query(Order.price, Order.base_quantity)
                                 .filter(Order.pair_id == pair_id,
                                         Order.direction == 'BID',
                                         or_(Order.status == 'ORDER_PENDING',
                                             Order.status == 'ORDER_PARTIAL_FILLED'))
                                 .order_by(Order.price.desc()))
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

    def query_open_order_count_by_pairid_and_address(self, client_address=None, pair_id=None, limit_records=5) -> int:
        conditions = self.__get_open_order_conditions(client_address, pair_id)
        return (self.session.query(Order.pair_id, Order.owner, func.count(Order.id).label('order_count'))
                            .filter(and_(*conditions))
                            .group_by(Order.pair_id, Order.owner)
                            .order_by(text('order_count DESC'))
                            .limit(limit_records)
                            .all())

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
                             .filter(and_(Position.mark_price!=0, Position.mark_price!=None))
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

    def get_funding_transfers(self, address: str=None, pair_id: str=None, from_datetime: datetime.datetime=None):
        limit_records = 100

        conditions = []
        if address:
            conditions.append(FundingTransfer.owner==address)
        if pair_id:
            conditions.append(FundingTransfer.pair_id==pair_id)
        if from_datetime:
            conditions.append(Block.time>=from_datetime)

        query = (self.session.query(FundingTransfer, Block.time)
                             .join(Block, FundingTransfer.block_height==Block.height)
                             .filter(*conditions)
                             .order_by(Block.height.asc())
                             .limit(limit_records))
        return query.all()

    def update_realized_pnl_logs(self, start_block_height: int, end_block_height: int):
        update_query = """
        INSERT INTO realized_pnl_log
            SELECT owner, pair_id, SUM(realized_pnl) AS realized_pnl, SUM(funding_gain) AS funding_gain, SUM(liquidated_margin) AS liquidated_margin, :end_block_height AS block_height FROM (
                SELECT
                    COALESCE(q1.owner, q2.owner, q3.owner, q4.owner) AS owner,
                    COALESCE(q1.pair_id, q2.pair_id, q3.pair_id, q4.pair_id) AS pair_id,
                    COALESCE(q1.realized_pnl, 0) + COALESCE(q4.realized_pnl, 0) AS realized_pnl,
                    COALESCE(q2.funding_fee, 0) + COALESCE(q4.funding_gain, 0) AS funding_gain,
                    COALESCE(q3.margin, 0) + COALESCE(q4.liquidated_margin, 0) AS liquidated_margin,
                    :end_block_height AS block_height
                FROM
                    (SELECT
                        p.owner,
                        p.pair_id,
                        SUM(p.realized_pnl) AS realized_pnl
                    FROM positioning p
                    LEFT JOIN block b on p.block_height=b.height
                    WHERE
                        p.block_height BETWEEN :start_block_height AND :end_block_height
                        AND COALESCE(p.is_batch_update, FALSE) = FALSE
                    GROUP BY 1,2) q1
                FULL OUTER JOIN
                    (SELECT
                        f.owner,
                        f.pair_id,
                        SUM(funding_fee) AS funding_fee
                    FROM funding_transfer f
                    WHERE
                        f.block_height BETWEEN :start_block_height AND :end_block_height
                    GROUP BY 1,2) q2 ON q1.owner=q2.owner AND q1.pair_id=q2.pair_id
                FULL OUTER JOIN
                    (SELECT
                        p.owner,
                        p.pair_id,
                        SUM(margin) AS margin
                    FROM position p
                    WHERE
                        p.block_height BETWEEN :start_block_height AND :end_block_height
                        AND p.status='liquidated'
                    GROUP BY 1,2) q3 ON q1.owner=q3.owner AND q1.pair_id=q3.pair_id
                FULL OUTER JOIN
                    (SELECT DISTINCT ON (owner, pair_id) owner, pair_id, realized_pnl, funding_gain, liquidated_margin, block_height
                    FROM realized_pnl_log
                    ORDER BY owner ASC, pair_id ASC, block_height DESC) q4 ON q1.owner=q4.owner AND q1.pair_id=q4.pair_id
                ) q
            GROUP BY 1,2
        """

        self.session.execute(update_query, params=
        {
            'start_block_height': start_block_height,
            'end_block_height': end_block_height
        })
        self.session.commit()

    def delete_data(self, from_block_height: int, verbose=True):
        """Deletes all data starting from block height"""
        if not from_block_height:
            if verbose:
                logging.info('No initial block height specified, delete_data() did not remove any data')
            return

        delete_query = """
        DO $$
        DECLARE bh integer;
        BEGIN
            SELECT :from_block_height INTO bh;

            DELETE FROM block WHERE height>=bh;
            DELETE FROM funding_transfer WHERE block_height>=bh;
            DELETE FROM orderbook WHERE block_height>=bh;
            DELETE FROM orders WHERE block_height>=bh;
            DELETE FROM position WHERE block_height>=bh;
            DELETE FROM trade WHERE block_height>=bh;
            DELETE FROM orderbook_top WHERE block_height>=bh;
            DELETE FROM positioning WHERE block_height>=bh;
            DELETE FROM error WHERE block_height>=bh;
            DELETE FROM transfer WHERE block_height>=bh;
            DELETE FROM margin WHERE block_height>=bh;
            DELETE FROM oracle_price WHERE block_height>=bh;
            DELETE FROM realized_pnl_log wHERE block_height>=bh;

            UPDATE error_log SET height=el.height
            FROM (SELECT CASE WHEN bh<height THEN bh-1 ELSE height END as height FROM error_log) el;
        END $$;"""

        self.session.execute(delete_query, params={'from_block_height': from_block_height})
        self.session.commit()
        if verbose:
            logging.info(f'All data from {from_block_height} onward (inclusive) removed from database')

    def query_latest_block_height(self):
        """Query latest valid block height from database (where both `block_processed` and `tx_events_processed` are true)"""
        return (self.session.query(func.max(Block.height))
                    .filter(and_(Block.tx_events_processed==True, Block.block_processed==True))
                    .scalar())

    def query_lowest_incomplete_height(self):
        """Query lowest block height where either `block_processed` or `tx_events_processed` is false (i.e. block processing is incomplete)"""
        return (self.session.query(func.min(Block.height))
                            .filter(or_(Block.block_processed==False, Block.tx_events_processed==False))
                            .scalar())

    def delete_data_from_lowest_incomplete_height(self):
        """Deletes data from max block height (i.e. removes topmost block data)"""
        block_height = self.query_lowest_incomplete_height()
        self.delete_data(block_height)
            