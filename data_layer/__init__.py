from data_layer.model import metadata
from data_layer.engine import Engine

from data_layer.model import Cashier
from data_layer.model import Customer
from data_layer.model import Store
from data_layer.model import Vat
from data_layer.model import ProductUnit
from data_layer.model import DepartmentMainGroup
from data_layer.model import DepartmentSubGroup
from data_layer.model import Product
from data_layer.model import ProductBarcode
from data_layer.model import ProductBarcodeMask
from data_layer.model import TransactionHead
from data_layer.model import TransactionHeadTemp
from data_layer.model import TransactionProduct
from data_layer.model import TransactionProductTemp
from data_layer.model import TransactionPayment
from data_layer.model import TransactionPaymentTemp
from data_layer.model import TransactionTotal
from data_layer.model import TransactionTotalTemp
from data_layer.model import TransactionDiscount
from data_layer.model import TransactionDiscountTemp
from data_layer.model import Closure
from data_layer.model import ClosureTotal
from data_layer.model import ClosureCurrency


def init_db():
    temp_engine = Engine()
    metadata.create_all(bind=temp_engine.engine)
