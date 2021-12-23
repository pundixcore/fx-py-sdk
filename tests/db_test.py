import unittest
import decimal
from fx_py_sdk.model.model import *
from fx_py_sdk.model.crud import *

class MyTestCase(unittest.TestCase):
    def test_create_database(self):
        sql = Sql()
        sql.create_db("fxdex")

    def test_create_table(self):
        sql = Sql()
        sql.create_table("fxdex")

    def test_create_table_by_sqla(self):
        sql = Sql(database="fxdex")
        sql.create_table_by_sqla()

    def test_drop_table_by_sqla(self):
        sql = Sql(database="fxdex")
        sql.drop_table()


    def test_add(self):
        sql = Crud()
        order_id = "ID-1892-6"
        order = Order(
            block_number=100,
            tx_hash="84E6164550DF980D4FD7AEA68E3B2E3C608B7ADFB730A69C75EEC372CC706D59",
            owner="dex1n58mly6f7er0zs6swtetqgfqs36jaarqlhs528",
            order_id=order_id,
            pair_id="tsla:usdt",
            price=decimal.Decimal(100)
        )
        print(order.to_dict())
        sql.insert(order)
        order = sql.filterone(Order, Order.order_id==order_id)
        print(order.to_dict())


if __name__ == '__main__':
    unittest.main()
