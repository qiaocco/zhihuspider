from sqlalchemy import Column, Integer, String

from db.basic import Base, session


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
    is_crawled = Column(Integer, default=0)

    @classmethod
    def get_seed_names(cls):
        return session.query(cls.name).filter_by(is_crawled=0)

    @classmethod
    def set_seed_crawled(cls, user_name, result):
        seed = session.query(cls).filter(cls.name == user_name).first()
        if seed:
            seed.is_crawled = result
        else:
            seed = cls()
            seed.name = user_name
            seed.is_crawled = result
            session.add(seed)
        session.commit()
