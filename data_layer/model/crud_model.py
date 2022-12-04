from sqlalchemy.orm import declarative_base
from sqlalchemy import func

from data_layer.engine import Engine


Model = declarative_base()
metadata = Model.metadata


class CRUD:
    def __init__(self):
        self.engine = Engine()

    def filter_by(self, *args, **kwargs):
        return self.engine.session.query(type(self)).filter_by(*args, **kwargs)

    def save(self):
        if self.id is None:
            self.id = self.engine.session.query(func.max(type(self).id)).scalar() or 1
        self.engine.session.add(self)
        return self.engine.session.commit()
