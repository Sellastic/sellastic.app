from sqlalchemy import Column, Integer, BigInteger, Boolean, String, DateTime, Float, ForeignKey
from sqlalchemy.sql import func

from data_layer.model.crud_model import Model
from data_layer.model.crud_model import CRUD


class TransactionDiscountTemp(Model, CRUD):
    def __init__(self):
        Model.__init__(self)
        CRUD.__init__(self)

    __tablename__ = "transaction_discount_temp"

    id = Column(BigInteger, primary_key=True, autoincrement=True, default=1)
    fk_transaction_head_id = Column(BigInteger, ForeignKey("transaction_head_temp.id"))
    fk_transaction_product_id = Column(BigInteger, ForeignKey("transaction_product_temp.id"), nullable=True)
    fk_transaction_payment_id = Column(BigInteger, ForeignKey("transaction_payment_temp.id"), nullable=True)
    fk_transaction_total_id = Column(BigInteger, ForeignKey("transaction_total_temp.id"), nullable=True)
    line_no = Column(Integer, nullable=False)
    discount_type = Column(String(50), nullable=False)
    discount_amount = Column(Float, nullable=False)
    discount_rate = Column(Float, nullable=True)
    discount_code = Column(String(15), nullable=True)
    is_cancel = Column(Boolean, nullable=False, default=False)
    is_deleted = Column(Boolean, nullable=False, default=False)
    delete_description = Column(String(1000), nullable=True)
    fk_cashier_create_id = Column(BigInteger, ForeignKey("cashier.id"))
    fk_cashier_update_id = Column(BigInteger, ForeignKey("cashier.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<TransactionDiscountTemp(discount_type='{self.discount_type}', discount_amount='{self.discount_amount}')>"
