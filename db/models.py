from sqlalchemy import Column, Integer, String, text

from db.basic import Base, session
from decorators import db_commit_decorator


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
    approve = Column(Integer)  # 赞同数
    thanks = Column(Integer)  # 感谢数
    collect = Column(Integer)  # 收藏数
    image_url = Column(String(200))  # 头像url

    @classmethod
    def get_user_by_name(cls, name):
        return session.query(cls).filter(User.name == name).first()


class SeedUser(Base):
    __tablename__ = "seed_users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))  # 种子用户的用户名
    home_crawled = Column(
        Integer, server_default=text("0")
    )  # 首页抓取状态 0:未抓取, 1:抓取成功, 2: 抓取失败
    other_crawled = Column(Integer, server_default=text("0"))  # 粉丝关注抓取状态

    @classmethod
    def get_seed_names(cls):
        q = session.query(cls.name).filter_by(home_crawled=0)
        return q, session.query(q.exists()).scalar()

    @classmethod
    @db_commit_decorator
    def set_home_crawled(cls, user_name, result):
        seed = session.query(cls).filter(cls.name == user_name).first()
        if seed:
            seed.home_crawled = result
        else:
            seed = cls()
            seed.name = user_name
            seed.home_crawled = result
            session.add(seed)
        session.commit()

    @classmethod
    def get_seed_by_name(cls, user_name):
        return session.query(cls).filter(cls.name == user_name).first()

    @classmethod
    @db_commit_decorator
    def insert_many(cls, user_names):
        for name in user_names:
            if not cls.get_seed_by_name(name):
                seed = cls()
                seed.name = name
                session.add(seed)
                session.flush()
        session.commit()

    @classmethod
    @db_commit_decorator
    def set_other_crawled(cls, user_name, result):
        seed = cls.get_seed_by_name(user_name)
        seed.other_crawled = result
        session.commit()


class HotList(Base):
    __tablename__ = "hot_lists"

    id = Column(Integer, primary_key=True)
    hot_num = Column(Integer)  # 热度，单位：万
    title = Column(String(200))  # 标题
    excerpt = Column(String(500))  # 引用
    answer_count = Column(Integer)  # 回答数
    comment_count = Column(Integer)  # 评论数
    follower_count = Column(Integer)  # 关注数
    url = Column(String(200))  # 链接
    category = Column(String(100))  # 类型
