import unittest

from fx_py_sdk.model.model import Sql


class MyTestCase(unittest.TestCase):
    def test_create_database(self):
        sql = Sql()
        sql.create_db("fxdex")

    def test_create_table(self):
        sql = Sql()
        sql.create_table("fxdex")

if __name__ == '__main__':
    unittest.main()
