from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.sql import func

from data_layer.model.crud_model import Model
from data_layer.model.crud_model import CRUD


class ProductBarcodeMask(Model, CRUD):
    def __init__(self):
        Model.__init__(self)
        CRUD.__init__(self)

    __tablename__ = "product_barcode_mask"

    id = Column(BigInteger, primary_key=True, autoincrement=True, default=1)
    fk_product_id = Column(BigInteger, ForeignKey("product.id"))
    code_started_at = Column(Integer, nullable=True)
    code_length = Column(Integer, nullable=True)
    quantity_started_at = Column(Integer, nullable=True)
    quantity_length = Column(Integer, nullable=True)
    weight_started_at = Column(Integer, nullable=True)
    weight_length = Column(Integer, nullable=True)
    price_started_at = Column(Integer, nullable=True)
    price_length = Column(Integer, nullable=True)
    color_started_at = Column(Integer, nullable=True)
    color_length = Column(Integer, nullable=True)
    size_started_at = Column(Integer, nullable=True)
    size_length = Column(Integer, nullable=True)
    description = Column(String(150), nullable=True)
    fk_cashier_create_id = Column(BigInteger, ForeignKey("cashier.id"))
    fk_cashier_update_id = Column(BigInteger, ForeignKey("cashier.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<ProductBarcode(name='{self.name}', barcode='{self.barcode}'>"
