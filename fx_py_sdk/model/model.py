# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fx_py_sdk import constants
import os
import logging

Base = declarative_base()

def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

Base.to_dict = to_dict

class Order(Base):
    __tablename__ = 'orders'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    block_height = Column(Integer)
    tx_hash = Column(String(66))
    order_id = Column(String(100), nullable=False, unique=True)
    owner = Column(String(42))
    pair_id = Column(String(20))
    direction = Column(String(10))
    price = Column(Numeric)
    base_quantity = Column(Numeric)
    quote_quantity = Column(Numeric)
    filled_quantity = Column(Numeric)
    filled_avg_price = Column(Numeric)
    remain_locked = Column(Numeric)
    created_at = Column(DateTime)
    leverage = Column(Integer)
    status = Column(String(50))
    order_type = Column(String(50))
    cost_fee = Column(Numeric)
    locked_fee = Column(Numeric)
    cancel_block_height = Column(Integer)
    cancel_time = Column(DateTime)

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
    unrealized_pnl = Column(Numeric)
    margin_rate = Column(Numeric)
    initial_margin = Column(Numeric)
    pending_order_quantity = Column(Numeric)
    status = Column(String(20))  # open, close
    open_height = Column(Integer)
    close_height = Column(Integer)

class Orderbook(Base):
    __tablename__ = 'orderbook'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    price = Column(Numeric)
    quantity = Column(Numeric)
    direction = Column(String(20))
    pair_id = Column(String(20))

class Trade(Base):
    __tablename__ = 'trade'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    block_height = Column(Integer)
    deal_price = Column(Numeric)
    matched_quantity = Column(Numeric)
    order_id = Column(String(100), nullable=False, unique=True)
    owner = Column(String(42))
    pair_id = Column(String(20))
    direction = Column(String(10))
    price = Column(Numeric)  #entry price
    base_quantity = Column(Numeric)
    quote_quantity = Column(Numeric)
    filled_quantity = Column(Numeric)
    filled_avg_price = Column(Numeric)
    order_type = Column(String(50))
    cost_fee = Column(Numeric)
    locked_fee = Column(Numeric)

class FundingTransfer(Base):
    __tablename__ = 'funding_transfer'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    position_id = Column(Integer)
    pair_id = Column(String(20))
    owner = Column(String(42))
    funding_fee = Column(Numeric)
    block_height = Column(Integer)

class Block(Base):
    __tablename__ = 'block'
    height = Column('height', Integer, primary_key=True, autoincrement=False)
    time = Column(DateTime)

class Tx(Base):
    __tablename__ = 'tx'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    sender = Column(String(50))
    send_time = Column(String(50))
    type = Column(String(50))  # send_coin, create_order, close_position_order, cancel_order
    tx_hash = Column(String(66))
    result = Column(String(66))  # error, success

class Sql:
    def __init__(self, database: str = "postgres", user: str = "postgres", password: str = "123456", host: str = "localhost",
                 port: str = "5432"):

        try:
            database_env = os.environ[constants.DB.Database]
            user_env = os.environ[constants.DB.User]
            password_env = os.environ[constants.DB.Password]
            host_env = os.environ[constants.DB.Host]
            port_env = os.environ[constants.DB.Port]
            if len(database_env) > 0:
                database = database_env
            if len(user_env) > 0:
                user = user_env
            if len(password_env) > 0:
                password = password_env
            if len(host_env) > 0:
                host = host_env
            if len(port_env) > 0:
                port = port_env
        except Exception as e:
            logging.warn(f'Could not instantiate db from environment {e}')
        
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connect(database)

    def connect(self, db: str):
        """ Connect to the PostgreSQL database server """

        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(self.user, self.password, self.host, self.port, db)
        print(url)
        self.engine = sqlalchemy.create_engine(url, client_encoding='utf8')
        self.meta = sqlalchemy.MetaData(bind=self.engine)
        self.session = sessionmaker(bind=self.engine)

    def create_table(self):
        Base.metadata.create_all(self.engine)

    def drop_table(self):
        Base.metadata.drop_all(self.engine)

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
