from functools import wraps

from db.basic import session
from logger import storage


def db_commit_decorator(func):
    @wraps(func)
    def session_commit(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            storage.exception(f"db operation error, here is the detail {e}")
            session.rollback()

    return session_commit
