from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.sql import func

from data_layer.model.crud_model import Model
from data_layer.model.crud_model import CRUD


class ProductBarcode(Model, CRUD):
    def __init__(self):
        Model.__init__(self)
        CRUD.__init__(self)

    __tablename__ = "product_barcode"

    id = Column(BigInteger, primary_key=True, autoincrement=True, default=1)
    fk_product_id = Column(BigInteger, ForeignKey("product.id"))
    barcode = Column(String(50), nullable=False)
    is_allowed_negative_stock = Column(Boolean, nullable=False)
    is_allowed_return = Column(Boolean, nullable=False)
    purchase_price = Column(Float, nullable=True)
    price = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    description = Column(String(150), nullable=True)
    fk_cashier_create_id = Column(BigInteger, ForeignKey("cashier.id"))
    fk_cashier_update_id = Column(BigInteger, ForeignKey("cashier.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<ProductBarcode(name='{self.name}', barcode='{self.barcode}'>"
