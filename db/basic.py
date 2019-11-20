from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.conf import get_db_args

db_args = get_db_args()


# 初始化数据库连接:
connect_str = (
    f"{db_args['db_type']}+pymysql://{db_args['user']}:{db_args['password']}"
    f"@{db_args['host']}:{db_args['port']}/{db_args['db_name']}"
)
engine = create_engine(connect_str, echo=True)
# 创建对象的基类:
Base = declarative_base()
# 创建DBSession类型:
Session = sessionmaker(bind=engine)
