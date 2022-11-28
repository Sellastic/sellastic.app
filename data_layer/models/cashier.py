from sqlalchemy import Column, Integer, String, Boolean
from data_layer.models.model import Model


class Cashier(Model):
    __tablename__ = "cashier"

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False,)
    name = Column(String(50), nullable=False,)
    last_name = Column(String(50), nullable=False,)
    password = Column(String(50), nullable=False,)
    identity_number = Column(String(24))
    description = Column(String(100))
    is_administrator = Boolean(False)
    is_active = Boolean(False)

    def __repr__(self):
        return f"<User(name='{self.name}', last_name='{self.last_name}', user_name='{self.user_name}')>"

