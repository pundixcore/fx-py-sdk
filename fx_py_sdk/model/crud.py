from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from fx_py_sdk.model.model import Sql

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

    def update(self, object, filter, updic):
        self.session.query(object).filter(filter).update(updic)
        self.session.commit()


