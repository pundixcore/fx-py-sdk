# -*- coding: utf-8 -*-
import psycopg2

"""
if pip install psycopg2 have problem, try this: 
    ubuntu: install postgresql-devel 
    macos: brew install postgresql
"""


class Sql:
    def __init__(self, database: str = "postgres", user: str = "postgres", pw: str = "123456", host: str = "127.0.0.1",
                 port: str = "5432"):
        self.database = database
        self.user = user
        self.pw = pw
        self.host = host
        self.port = port
        self.conn = None
        self.connect()

    def connect(self):
        """ Connect to the PostgreSQL database server """
        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(database='fxdex', user=self.user, password=self.pw, host=self.host,
                                         port=self.port)
            # create a cursor
            cur = self.conn.cursor()

            # execute a statement
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)

            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("db connect: ", error)

    def create_db(self, db: str):
        self.conn = psycopg2.connect(database=self.database, user=self.user, password=self.pw, host=self.host,
                                     port=self.port)
        self.conn.autocommit = True
        cursor = self.conn.cursor()
        sql = "CREATE database %s" % db
        cursor.execute(sql)
        print("Database created successfully........")
        self.conn.close()

    def create_table(self, db: str):
        commands = (
            '''DROP TABLE if EXISTS orders''',
            '''CREATE TABLE orders(
                       id serial4 PRIMARY KEY,
                       block_number INT,
                       tx_hash varchar(20) not NULL,
                       order_id varchar(20),
                       owner varchar(42),
                       pair_id varchar(10),
                       direction varchar(10),
                       price FLOAT,
                       base_quantity FLOAT,
                       quote_quantity FLOAT,
                       filled_quantity FLOAT,
                       filled_avg_price FLOAT ,
                       remain_locked FLOAT ,
                       created_at varchar(50),
                       leverage INT,
                       status  varchar(30),
                       order_type varchar(30),
                       cost_fee FLOAT ,
                       locked_fee FLOAT);''',
            '''create unique index idx_orders_order_id   on orders using btree (order_id);''',


            '''DROP TABLE if EXISTS positions;''',
            '''CREATE TABLE positions(
                       id serial4 PRIMARY KEY,
                       position_id varchar(20) not NULL,
                       owner varchar(42),
                       pair_id varchar(10),
                       direction varchar(10),
                       entry_price  FLOAT,
                       mark_price FLOAT,
                       liquidation_price FLOAT,
                       base_quantity FLOAT,
                       margin FLOAT,
                       leverage INT,
                       unrealized_pnl FLOAT,
                       margin_rate FLOAT,
                       initial_margin FLOAT,
                       pending_order_quantity FLOAT);''',
            '''create unique index idx_positions_position_id on positions using btree (position_id);''',


            """DROP TABLE if EXISTS orderbook;""",
            '''CREATE TABLE orderbook(
                       id serial4 PRIMARY KEY,
                       price FLOAT ,
                       quantity FLOAT ,
                       type varchar(10));'''
            '''create unique index idx_orderbook_price on orderbook using btree (price);''',

            """DROP TABLE if EXISTS block;""",
            '''CREATE TABLE block(
                       number serial4 PRIMARY KEY);'''
        )
        try:
            # self.conn = psycopg2.connect(database=db, user=self.user, password=self.pw, host=self.host,
            #                              port=self.port)

            cur = self.conn.cursor()
            # create table one by one
            for command in commands:
                cur.execute(command)
            cur.close()
            self.conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print("sql caught: ", error)

        finally:
            if self.conn is not None:
                self.conn.close()
