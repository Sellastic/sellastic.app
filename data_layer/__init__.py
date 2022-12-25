from data_layer.model import metadata
from data_layer.engine import Engine

from data_layer.model import Cashier
from data_layer.model import Store
from data_layer.model import Vat
from data_layer.model import ProductUnit
from data_layer.model import DepartmentMainGroup
from data_layer.model import DepartmentSubGroup
from data_layer.model import Product
from data_layer.model import ProductBarcode
from data_layer.model import ProductBarcodeMask
from data_layer.model import TransactionHead


def init_db():
    temp_engine = Engine()
    metadata.create_all(bind=temp_engine.engine)
