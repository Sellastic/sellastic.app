from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from data_layer.model.crud_model import Model
from data_layer.model.crud_model import CRUD


class ProductUnit(Model, CRUD):
    def __init__(self, name=None, no: int = None, description: str = None,
                 base_id: int = None, base_amount: float = None, symbol: str = None):
        Model.__init__(self)
        CRUD.__init__(self)

        self.name = name
        self.no = no
        self.description = description
        self.base_id = base_id
        self.base_amount = base_amount
        self.symbol = symbol

    __tablename__ = "product_unit"

    id = Column(BigInteger, primary_key=True, autoincrement=True, default=1)
    name = Column(String(50), nullable=False)
    no = Column(Integer, nullable=False)
    description = Column(String(100), nullable=False)
    base_id = Column(Integer, nullable=False)
    base_amount = Column(Float, nullable=False)
    symbol = Column(String(10), nullable=False)
    fk_cashier_create_id = Column(BigInteger, ForeignKey("cashier.id"))
    fk_cashier_update_id = Column(BigInteger, ForeignKey("cashier.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<ProductUnit(name='{self.name}', no='{self.no}', description='{self.description}')>"
