from data_layer.model import metadata
from data_layer.engine import Engine

from data_layer.model import Cashier
from data_layer.model import Vat
from data_layer.model import StockUnit
from data_layer.model import StockMainGroup


def init_db():
    temp_engine = Engine()
    metadata.create_all(bind=temp_engine.engine)
