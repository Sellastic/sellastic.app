from sqlalchemy import Column, BigInteger, String, Boolean, DateTime
from sqlalchemy.sql import func

from data_layer.model.crud_model import Model
from data_layer.model.crud_model import CRUD


class Cashier(Model, CRUD):
    def __init__(self, user_name=None, name=None, last_name=None, password=None,
                 identity_number=None, description=None, is_administrator=False, is_active=False):
        Model.__init__(self)
        CRUD.__init__(self)

        self.user_name = user_name
        self.name = name
        self.last_name = last_name
        self.password = password
        self.identity_number = identity_number
        self.description = description
        self.is_administrator = is_administrator
        self.is_active = is_active

    __tablename__ = "cashier"

    id = Column(BigInteger, primary_key=True, autoincrement=True, default=1)
    user_name = Column(String(50), unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    identity_number = Column(String(24))
    description = Column(String(100))
    is_deleted = Column(Boolean, nullable=False)
    delete_description = Column(String(1000), nullable=True)
    is_administrator = Column(Boolean(False), default=False)
    is_active = Column(Boolean(False), default=False)
    created_at = Column(DateTime, server_default=func.now())
    login_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<Cashier(name='{self.name}', last_name='{self.last_name}', user_name='{self.user_name}')>"

