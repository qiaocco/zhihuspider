from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.conf import get_db_args
from db.basic import Base


class User(Base):
    __tablename__ = "users"

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(100))  # 用户名
    headline = Column(String(200))  # 用户签名
    career = Column(String(100))  # 职业
    education = Column(String(200))  # 教育
    introduction = Column(String(200))  # 个人简介
    follower = Column(Integer)  # 关注数
    following = Column(Integer)  # 粉丝数
    image_url = Column(String(200))  # 头像url
