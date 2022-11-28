from sqlalchemy import create_engine
from data_layer.models.model import Model, metadata
from data_layer.models.cashier import Cashier

engine = create_engine('sqlite:///db.sqlite3', echo=True)
print(engine)


metadata.create_all(engine)
