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
        order = Order(
            block_number=100,
            order_id="ID-100-1",
            pair_id="tsla:usdt",
            price=decimal.Decimal(100)
        )
        sql.add(order)


if __name__ == '__main__':
    unittest.main()
