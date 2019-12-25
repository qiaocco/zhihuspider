from pymysql.err import IntegrityError as PymysqlIntegrityError
from sqlalchemy.exc import IntegrityError as SqlalchemyIntegrityError
from sqlalchemy.exc import InvalidRequestError

from db.basic import session
from decorators import db_commit_decorator


class CommonOperate:
    @classmethod
    @db_commit_decorator
    def add_one(cls, obj):
        session.add(obj)
        session.commit()

    @classmethod
    @db_commit_decorator
    def add_all(cls, datas):
        try:
            session.add_all(datas)
            session.commit()
        except (SqlalchemyIntegrityError, PymysqlIntegrityError, InvalidRequestError):
            for data in datas:
                cls.add_one(data)
