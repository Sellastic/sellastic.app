from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from data_layer.model.crud_model import Model
from data_layer.model.crud_model import CRUD


class DepartmentMainGroup(Model, CRUD):
    def __init__(self, name=None, no: int = None, description: str = None,
                 max_price: float = None, discount_rate: float = None):
        Model.__init__(self)
        CRUD.__init__(self)

        self.name = name
        self.no = no
        self.description = description
        self.max_price = max_price
        self.discount_rate = discount_rate

    __tablename__ = "department_main_group"

    id = Column(BigInteger, primary_key=True, autoincrement=True, default=1)
    name = Column(String(50), nullable=False)
    no = Column(Integer, nullable=False)
    fk_vat_id = Column(BigInteger, ForeignKey("vat.id"))
    description = Column(String(100), nullable=False)
    max_price = Column(Float, nullable=False)
    discount_rate = Column(Float, nullable=False)
    is_deleted = Column(Boolean, nullable=False)
    delete_description = Column(String(1000), nullable=True)
    fk_cashier_create_id = Column(BigInteger, ForeignKey("cashier.id"))
    fk_cashier_update_id = Column(BigInteger, ForeignKey("cashier.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<DepartmentMainGroup(name='{self.name}', no='{self.no}', description='{self.description}')>"
