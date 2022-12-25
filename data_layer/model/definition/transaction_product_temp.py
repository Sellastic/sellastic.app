from sqlalchemy import Column, Integer, BigInteger, Boolean, String, DateTime, Float, ForeignKey, UUID
from sqlalchemy.sql import func

from data_layer.model.crud_model import Model
from data_layer.model.crud_model import CRUD

from uuid import uuid4


class TransactionProductTemp(Model, CRUD):
    def __init__(self):
        Model.__init__(self)
        CRUD.__init__(self)

    __tablename__ = "transaction_product_temp"

    id = Column(BigInteger, primary_key=True, autoincrement=True, default=1)
    fk_transaction_head_id = Column(BigInteger, ForeignKey("transaction_head_temp.id"))
    line_no = Column(Integer, nullable=False)
    fk_department_main_group_id = Column(BigInteger, ForeignKey("department_main_group.id"), nullable=False)
    fk_department_sub_group_id = Column(BigInteger, ForeignKey("department_main_group.id"), nullable=True)
    fk_product_id = Column(BigInteger, ForeignKey("product.id"), nullable=True)
    fk_product_barcode_id = Column(BigInteger, ForeignKey("product_barcode.id"), nullable=True)
    fk_product_barcode_mask_id = Column(BigInteger, ForeignKey("product_barcode_mask.id"), nullable=True)
    vat_rate = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    unit_discount = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
    total_vat = Column(Float, nullable=False)
    total_discount = Column(Float, nullable=True)
    is_cancel = Column(Boolean, nullable=False, default=False)
    is_deleted = Column(Boolean, nullable=False, default=False)
    delete_description = Column(String(1000), nullable=True)
    fk_cashier_create_id = Column(BigInteger, ForeignKey("cashier.id"))
    fk_cashier_update_id = Column(BigInteger, ForeignKey("cashier.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<TransactionProductTemp(total_price='{self.total_price}')>"
