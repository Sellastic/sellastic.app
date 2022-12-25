from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.sql import func

from data_layer.model.crud_model import Model
from data_layer.model.crud_model import CRUD


class Product(Model, CRUD):
    def __init__(self):
        Model.__init__(self)
        CRUD.__init__(self)

    __tablename__ = "product"

    id = Column(BigInteger, primary_key=True, autoincrement=True, default=1)
    name = Column(String(50), nullable=False)
    short_name = Column(String(50), nullable=True)
    code = Column(Integer, nullable=False)
    old_code = Column(Integer, nullable=True)
    keyboard_value = Column(String(10), nullable=True)
    description = Column(String(150), nullable=True)
    description_on_screen = Column(String(150), nullable=True)
    description_on_shelf = Column(String(150), nullable=True)
    description_on_scale = Column(String(150), nullable=True)
    is_scalable = Column(Boolean, nullable=False)
    is_allowed_free_discount = Column(Boolean, nullable=False)
    is_allowed_negative_stock = Column(Boolean, nullable=False)
    is_allowed_return = Column(Boolean, nullable=False)
    purchase_price = Column(Float, nullable=True)
    price = Column(Float, nullable=False)
    discount_rate = Column(Float, nullable=False)
    stock_number = Column(Integer, nullable=False)
    alert_min_stock_number = Column(Integer, nullable=False)
    alert_max_stock_number = Column(Integer, nullable=False)
    fk_vat_id = Column(BigInteger, ForeignKey("vat.id"))
    fk_product_unit_id = Column(BigInteger, ForeignKey("product_unit.id"))
    fk_department_main_group_id = Column(BigInteger, ForeignKey("department_main_group.id"))
    fk_department_sub_group_id = Column(BigInteger, ForeignKey("department_sub_group.id"))
    fk_store_id = Column(BigInteger, ForeignKey("store.id"))
    is_deleted = Column(Boolean, nullable=False)
    delete_description = Column(String(1000), nullable=True)
    fk_cashier_create_id = Column(BigInteger, ForeignKey("cashier.id"))
    fk_cashier_update_id = Column(BigInteger, ForeignKey("cashier.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<Product(name='{self.name}', code='{self.code}', price='{self.price}')>"
