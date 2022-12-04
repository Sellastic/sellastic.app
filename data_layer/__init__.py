from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_layer.model.model import Model, metadata
from data_layer.model.cashier import Cashier

engine = create_engine('sqlite:///db.sqlite3', echo=True)
print(engine)

session = sessionmaker(bind=engine)()


def init_db():
    metadata.create_all(bind=engine)
