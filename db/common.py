from db.basic import session


class CommonOperate:
    @classmethod
    def add_one(cls, obj):
        session.add(obj)
        session.commit()
