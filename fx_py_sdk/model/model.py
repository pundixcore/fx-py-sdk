# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy import Index, Table, Column, Integer, String, Boolean, ForeignKey, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fx_py_sdk import constants
import os
import logging
import pandas as pd

Base = declarative_base()

def to_dict(self):
    dict_attrs = dict()
    for col in self.__table__.columns:
        attr = getattr(self, col.name, None)
        if attr is not None:
            dict_attrs[col.name] = attr
    return dict_attrs

Base.to_dict = to_dict

class Order(Base):
    __tablename__ = 'orders'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    block_height = Column(Integer, index=True)
    tx_hash = Column(String(66))
    order_id = Column(String(100), nullable=False, unique=True)
    owner = Column(String(42))
    liquidation_owner = Column(String(42))
    pair_id = Column(String(20), index=True)
    direction = Column(String(10))
    price = Column(Numeric)
    base_quantity = Column(Numeric)
    quote_quantity = Column(Numeric)
    filled_quantity = Column(Numeric)
    last_filled_quantity = Column(Numeric)
    filled_avg_price = Column(Numeric)
    remain_locked = Column(Numeric)
    created_at = Column(DateTime)
    leverage = Column(Integer)
    status = Column(String(50), index=True)
    order_type = Column(String(50))
    cost_fee = Column(Numeric)
    locked_fee = Column(Numeric)
    open_block_height = Column(Integer)
    cancel_block_height = Column(Integer)
    filled_block_height = Column(Integer)
    cancel_time = Column(DateTime)
    block_height = Column(Integer)
    initial_base_quantity = Column(Numeric)

class Position(Base):
    __tablename__ = 'position'

    # id = Column('id', Integer, primary_key=True, autoincrement=True)
    position_id = Column(Integer, primary_key=True, nullable=False)
    owner = Column(String(42))
    pair_id = Column(String(20))
    direction = Column(String(10))
    entry_price = Column(Numeric)
    mark_price = Column(Numeric)
    liquidation_price = Column(Numeric)
    base_quantity = Column(Numeric)
    margin = Column(Numeric)
    leverage = Column(Integer)
    realized_pnl = Column(Numeric)
    unrealized_pnl = Column(Numeric)
    margin_rate = Column(Numeric)
    initial_margin = Column(Numeric)
    pending_order_quantity = Column(Numeric)
    status = Column(String(20))  # open, close
    open_height = Column(Integer)
    close_height = Column(Integer)
    block_height = Column(Integer)
    last_order_fill_height = Column(Integer)

class Orderbook(Base):
    __tablename__ = 'orderbook'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    price = Column(Numeric)
    quantity = Column(Numeric)
    direction = Column(String(20))
    pair_id = Column(String(20))
    block_height = Column(Integer)

class Trade(Base):
    __tablename__ = 'trade'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    block_height = Column(Integer, index=True)
    deal_price = Column(Numeric)
    matched_quantity = Column(Numeric)
    order_id = Column(String(100), nullable=False, unique=False)
    owner = Column(String(42), index=True)
    liquidation_owner = Column(String(42))
    pair_id = Column(String(20), index=True)
    direction = Column(String(10), index=True)
    price = Column(Numeric)  #entry price
    base_quantity = Column(Numeric)
    quote_quantity = Column(Numeric)
    filled_quantity = Column(Numeric)
    filled_avg_price = Column(Numeric)
    order_type = Column(String(50))
    cost_fee = Column(Numeric)
    locked_fee = Column(Numeric)
    block_height = Column(Integer)

class FundingTransfer(Base):
    __tablename__ = 'funding_transfer'
    __table_args__ = (
        Index('ix_funding_transfer_owner_pairid_height', 'owner', 'pair_id', 'block_height'),
    )

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    position_id = Column(Integer)
    pair_id = Column(String(20), index=True)
    owner = Column(String(42), index=True)
    funding_fee = Column(Numeric)
    block_height = Column(Integer)

class Block(Base):
    __tablename__ = 'block'
    height = Column('height', Integer, primary_key=True, index=True, autoincrement=False)
    time = Column(DateTime, index=True)
    block_processed = Column(Boolean, default=False, index=True)
    tx_events_processed = Column(Boolean, default=False, index=True)

class Tx(Base):
    __tablename__ = 'tx'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    sender = Column(String(50))
    send_time = Column(String(50))
    type = Column(String(50))  # send_coin, create_order, close_position_order, cancel_order
    tx_hash = Column(String(66))
    result = Column(String(66))  # error, success

""" auxillary helper classes """
class Positioning(Base):
    __tablename__ = 'positioning'
    __table_args__ = (
        Index('ix_positioning_owner_pairid_height', 'owner', 'pair_id', 'block_height'),
    )

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    owner = Column(String(42))
    pair_id = Column(String(20))
    entry_price = Column(Numeric)
    mark_price = Column(Numeric)
    base_quantity = Column(Numeric)
    realized_pnl = Column(Numeric)
    unrealized_pnl = Column(Numeric)
    margin = Column(Numeric)
    direction = Column(String(10))
    position_id = Column(Integer)
    locked_fees = Column(Numeric)
    block_height = Column(Integer)
    is_batch_update = Column(Boolean, default=False)

class Realized_Pnl_Log(Base):
    __tablename__ = 'realized_pnl_log'

    owner = Column(String(42), index=True, primary_key=True)
    pair_id = Column(String(42), index=True, primary_key=True)
    realized_pnl = Column(Numeric)
    funding_gain = Column(Numeric)
    liquidated_margin = Column(Numeric)
    block_height = Column(Integer, index=True, primary_key=True)

class Balance(Base):
    __tablename__ = 'balance'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    owner = Column(String(42))
    token = Column('pair_id', String(70), index=True)
    amount = Column(Numeric)
    batch_time = Column(DateTime)
    time = Column(DateTime)

class OrderbookTop(Base):
    __tablename__ = 'orderbook_top'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    pair_id = Column(String(20), index=True)
    best_bid = Column(Numeric)
    best_ask = Column(Numeric)
    block_height = Column(Integer)

class FundingRate(Base):
    __tablename__ = 'funding_rate'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    pair_id = Column(String(20), index=True)
    rate = Column(Numeric)
    funding_times = Column(Integer)
    block_height = Column(Integer)

class Wallet(Base):
    __tablename__ = 'wallet'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    address = Column(String(42), unique=True)
    owner = Column(String(100))
    pair_id = Column(String(20))
    comment = Column(String(256))
    leverage = Column(Integer)

class Margin(Base):
    __tablename__ = 'margin'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    add_amount = Column(Numeric)
    tx_hash = Column(String(66))
    position_id = Column(Integer, index=True)
    pair_id = Column(String(20), index=True)
    mark_price = Column(Numeric)
    base_quantity = Column(Numeric)
    direction = Column(String(10))
    owner = Column(String(100), index=True)
    leverage = Column(Integer)
    entry_price = Column(Numeric)
    liquidation_price = Column(Numeric)
    margin_rate = Column(Numeric)
    margin = Column(Numeric)
    block_height = Column(Integer)

class LockedFee(Base):
    __tablename__ = 'locked_fee'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    pair_id = Column(String(20), index=True)
    owner = Column(String(100), index=True)
    direction = Column(String(10))
    fees = Column(Numeric)
    block_height = Column(Integer)

class Error(Base):
    __tablename__ = 'error'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    sender = Column(String(42), index=True)
    log = Column(String(1024))
    block_height = Column(Integer, index=True)

class ErrorLog(Base):
    __tablename__ = 'error_log'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    height = Column(Integer)

class Transfer(Base):
    __tablename__ = 'transfer'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    sender = Column(String(100), index=True)
    recipient = Column(String(100), index=True)
    amount = Column(Numeric)
    token = Column(String(70), index=True)
    block_height = Column(Integer, index=True)

class OraclePrice(Base):
    __tablename__ = 'oracle_price'
    market_id = Column(String(20), primary_key=True, index=True)
    price = Column(Numeric)
    block_height = Column(Integer, primary_key=True, index=True)

class TradePair(Base):
    __tablename__ = 'trade_pair'
    pair_id = Column(String(20), primary_key=True)

class HedgingOrder(Base):
    __tablename__ = 'hedging_order'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    dex_order_id = Column(String(100))
    dex_trade_id = Column(Integer)
    order_id = Column(String(100))      # Hedging exchange order ID
    order_type = Column(String(50))
    status = Column(String(50), index=True)
    price = Column(Numeric)
    quantity = Column(Numeric)
    direction = Column(String(10))
    symbol = Column(String(20), index=True)
    exchange = Column(String(20), index=True)
    time = Column(DateTime)
    commission = Column(Numeric, default=0)
    gas_fee = Column(Numeric, default=0)

class HedgingTrade(Base):
    __tablename__ = 'hedging_trade'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    order_id = Column(String(100))      # Hedging exchange order ID
    trade_id = Column(String(100))      # Hedging exchange trade ID (if any)
    dex_trade_id = Column(Integer)
    order_type = Column(String(50))
    status = Column(String(50), index=True)
    price = Column(Numeric)
    quantity = Column(Numeric)
    direction = Column(String(10))
    symbol = Column(String(20), index=True)
    exchange = Column(String(20), index=True)
    time = Column(DateTime)

class Sql:
    def __init__(self, database: str = "postgres", user: str = "postgres", password: str = "123456", host: str = "localhost",
                 port: str = "5432"):

        database = os.environ.get(constants.DB.Database, database)
        user = os.environ.get(constants.DB.User, user)
        password = os.environ.get(constants.DB.Password, password)
        host = os.environ.get(constants.DB.Host, host)  # 47.90.177.191
        port = os.environ.get(constants.DB.Port, port)

        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        try:
            self.connect(database)
            logging.info(f'Connected to database {database}')
        except Exception as ex:
            logging.error(f'Failed connecting to database {database}: {ex}')

    def connect(self, db: str):
        """ Connect to the PostgreSQL database server """

        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(self.user, self.password, self.host, self.port, db)
        print(url)
        self.engine = sqlalchemy.create_engine(url, client_encoding='utf8')
        self.meta = sqlalchemy.MetaData(bind=self.engine)
        self.session = sessionmaker(bind=self.engine)

    def create_table(self):
        # Creates database schema
        Base.metadata.create_all(self.engine)

    def drop_table(self):
        # Terminates all processes connected to db
        self.engine.execute(f'''
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = '{self.database}'
AND pid <> pg_backend_pid();''')

        # Drop all tables
        Base.metadata.drop_all(self.engine)

    def initialize_table(self, csv_filename: str, table_name: str):
        try:
            df = pd.read_csv(csv_filename)
            df.to_sql(table_name, self.engine, if_exists='append', index=False)
        except:
            return

    def initialize_wallets(self):
        self.initialize_table('wallets.csv', 'wallet')

    def initialize_trade_pairs(self):
        self.initialize_table('trade_pairs.csv', 'trade_pair')

    def initialize_error_log_height(self, starting_height=None):
        with self.session() as session:
            if not starting_height:
                starting_height = session.execute('SELECT MAX(height) FROM block').first()[0] or 1

            session.execute(f'''
    INSERT INTO error_log (height)
    SELECT {starting_height}
    WHERE NOT EXISTS (SELECT * FROM error_log)''')
            session.commit()

    """
    Below is create database and table use psycopg2, require your computer install postgresql
    if pip install psycopg2 have problem, try this: 
        ubuntu: install postgresql-devel 
        macos: brew install postgresql
    """
    # def create_db(self, db: str):
    #     self.conn = psycopg2.connect(database=self.database, user=self.user, password=self.pw, host=self.host,
    #                                  port=self.port)
    #     self.conn.autocommit = True
    #     cursor = self.conn.cursor()
    #     sql = "CREATE database %s" % db
    #     cursor.execute(sql)
    #     print("Database created successfully........")
    #     self.conn.close()
    #
    # def create_table(self, db: str):
    #     commands = (
    #         '''DROP TABLE if EXISTS orders''',
    #         '''CREATE TABLE orders(
    #                    id serial4 PRIMARY KEY,
    #                    block_height INT,
    #                    tx_hash varchar(20) not NULL,
    #                    order_id varchar(20),
    #                    owner varchar(42),
    #                    pair_id varchar(10),
    #                    direction varchar(10),
    #                    price FLOAT,
    #                    base_quantity FLOAT,
    #                    quote_quantity FLOAT,
    #                    filled_quantity FLOAT,
    #                    filled_avg_price FLOAT ,
    #                    remain_locked FLOAT ,
    #                    created_at varchar(50),
    #                    leverage INT,
    #                    status  varchar(30),
    #                    order_type varchar(30),
    #                    cost_fee FLOAT ,
    #                    locked_fee FLOAT);''',
    #         '''create unique index idx_orders_order_id   on orders using btree (order_id);''',
    #
    #
    #         '''DROP TABLE if EXISTS positions;''',
    #         '''CREATE TABLE positions(
    #                    id serial4 PRIMARY KEY,
    #                    position_id varchar(20) not NULL,
    #                    owner varchar(42),
    #                    pair_id varchar(10),
    #                    direction varchar(10),
    #                    entry_price  FLOAT,
    #                    mark_price FLOAT,
    #                    liquidation_price FLOAT,
    #                    base_quantity FLOAT,
    #                    margin FLOAT,
    #                    leverage INT,
    #                    unrealized_pnl FLOAT,
    #                    margin_rate FLOAT,
    #                    initial_margin FLOAT,
    #                    pending_order_quantity FLOAT);''',
    #         '''create unique index idx_positions_position_id on positions using btree (position_id);''',
    #
    #
    #         """DROP TABLE if EXISTS orderbook;""",
    #         '''CREATE TABLE orderbook(
    #                    id serial4 PRIMARY KEY,
    #                    price FLOAT ,
    #                    quantity FLOAT ,
    #                    type varchar(10));'''
    #         '''create unique index idx_orderbook_price on orderbook using btree (price);''',
    #     )
    #     try:
    #         self.conn = psycopg2.connect(database=db, user=self.user, password=self.pw, host=self.host,
    #                                      port=self.port)
    #
    #         cur = self.conn.cursor()
    #         # create table one by one
    #         for command in commands:
    #             cur.execute(command)
    #         cur.close()
    #         self.conn.commit()
    #
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print("sql caught: ", error)
    #
    #     finally:
    #         if self.conn is not None:
    #             self.conn.close()
