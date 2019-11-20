import sys

from db.basic import Base, engine  # noqa
from db.models import *  # noqa

# to work well inside config module or outsize config module
sys.path.append("..")
sys.path.append(".")


def create_all_table():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_all_table()
