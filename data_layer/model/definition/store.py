from sqlalchemy import Column, BigInteger, String, Boolean, DateTime
from sqlalchemy.sql import func

from data_layer.model.crud_model import Model
from data_layer.model.crud_model import CRUD


class Store(Model, CRUD):
    def __init__(self, name=None, brand_name=None, company_name=None,
                 web_page_url=None, description=None):
        Model.__init__(self)
        CRUD.__init__(self)

        self.name = name
        self.brand_name = brand_name
        self.company_name = company_name
        self.web_page_url = web_page_url
        self.description = description

    __tablename__ = "store"

    id = Column(BigInteger, primary_key=True, autoincrement=True, default=1)
    name = Column(String(250), nullable=False)
    brand_name = Column(String(50), nullable=True)
    company_name = Column(String(50), nullable=True)
    web_page_url = Column(String(250), nullable=True)
    description = Column(String(100), nullable=True)
    is_deleted = Column(Boolean, nullable=False)
    delete_description = Column(String(1000), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<Store(name='{self.name}', brand_name='{self.brand_name}', company_name='{self.company_name}')>"

