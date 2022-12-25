from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer
from sqlalchemy.sql import func

from data_layer.model.crud_model import Model
from data_layer.model.crud_model import CRUD


class Customer(Model, CRUD):
    def __init__(self, name=None, last_name=None, address_line_1=None, address_line_2=None, address_line_3=None,
                 email_address=None, phone_number=None, zip_code=None, description=None):
        Model.__init__(self)
        CRUD.__init__(self)

        self.name = name
        self.last_name = last_name
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.address_line_3 = address_line_3
        self.email_address = email_address
        self.phone_number = phone_number
        self.zip_code = zip_code
        self.description = description

    __tablename__ = "customer"

    id = Column(BigInteger, primary_key=True, autoincrement=True, default=1)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    address_line_1 = Column(String(100), nullable=True)
    address_line_2 = Column(String(100), nullable=True)
    address_line_3 = Column(String(100), nullable=True)
    email_address = Column(String(100), nullable=True)
    phone_number = Column(String(100), nullable=True)
    zip_code = Column(String(50), nullable=True)
    description = Column(String(100))
    total_bonus_point = Column(Integer, nullable=False, default=0)
    is_deleted = Column(Boolean, nullable=False, default=False)
    delete_description = Column(String(1000), nullable=True)
    is_administrator = Column(Boolean(False), default=False)
    is_active = Column(Boolean(False), default=False)
    created_at = Column(DateTime, server_default=func.now())
    login_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<Customer(name='{self.name}', last_name='{self.last_name}')>"

