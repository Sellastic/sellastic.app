from sqlalchemy import Column, Integer, BigInteger, Boolean, String, DateTime, Float, ForeignKey
from sqlalchemy.sql import func

from data_layer.model.crud_model import Model
from data_layer.model.crud_model import CRUD


class Vat(Model, CRUD):
    def __init__(self, name=None, no: int = None, rate: float = None, description=None):
        Model.__init__(self)
        CRUD.__init__(self)

        self.name = name
        self.no = no
        self.rate = rate
        self.description = description

    __tablename__ = "vat"

    id = Column(BigInteger, primary_key=True, autoincrement=True, default=1)
    name = Column(String(50), nullable=False)
    no = Column(Integer, nullable=False)
    rate = Column(Integer, nullable=False)
    description = Column(String(100))
    is_deleted = Column(Boolean, nullable=False, default=False)
    delete_description = Column(String(1000), nullable=True)
    fk_cashier_create_id = Column(BigInteger, ForeignKey("cashier.id"))
    fk_cashier_update_id = Column(BigInteger, ForeignKey("cashier.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<Vat(name='{self.name}', no='{self.no}', rate='{self.rate}')>"
