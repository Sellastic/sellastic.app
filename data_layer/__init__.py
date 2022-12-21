from data_layer.model import metadata
from data_layer.engine import Engine

from data_layer.model.cashier import Cashier
from data_layer.model.vat import Vat


def init_db():
    temp_engine = Engine()
    metadata.create_all(bind=temp_engine.engine)
