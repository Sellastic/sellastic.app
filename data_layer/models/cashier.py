from sqlalchemy import Column, BigInteger, String, Boolean, DateTime
from sqlalchemy.sql import func

from data_layer.models.model import Model


class Cashier(Model):
    __tablename__ = "cashier"

    id = Column(BigInteger, primary_key=True, autoincrement="auto")
    user_name = Column(String(50), unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    identity_number = Column(String(24))
    description = Column(String(100))
    is_administrator = Column(Boolean(False))
    is_active = Column(Boolean(False))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<User(name='{self.name}', last_name='{self.last_name}', user_name='{self.user_name}')>"

