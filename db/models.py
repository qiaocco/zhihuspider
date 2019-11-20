from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.conf import get_db_args
from db.basic import Base


class User(Base):
    # 表的名字:
    __tablename__ = "user"

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
