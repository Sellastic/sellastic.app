from sqlalchemy import Column, Integer, BigInteger, Boolean, String, DateTime, Float, ForeignKey
from sqlalchemy.sql import func

from data_layer.model.crud_model import Model
from data_layer.model.crud_model import CRUD


class TransactionPayment(Model, CRUD):
    def __init__(self):
        Model.__init__(self)
        CRUD.__init__(self)

    __tablename__ = "transaction_payment"

    id = Column(BigInteger, primary_key=True, autoincrement=True, default=1)
    fk_transaction_head_id = Column(BigInteger, ForeignKey("transaction_head.id"))
    line_no = Column(Integer, nullable=False)
    payment_type = Column(String(50), nullable=False)
    payment_total = Column(Float, nullable=False)
    currency_code = Column(Integer, nullable=False)
    currency_total = Column(Float, nullable=False)
    currency_exchange_rate = Column(Float, nullable=False)
    installment_count = Column(Integer, nullable=False)
    payment_tool_id = Column(String(50), nullable=True)
    is_cancel = Column(Boolean, nullable=False, default=False)
    is_deleted = Column(Boolean, nullable=False, default=False)
    delete_description = Column(String(1000), nullable=True)
    fk_cashier_create_id = Column(BigInteger, ForeignKey("cashier.id"))
    fk_cashier_update_id = Column(BigInteger, ForeignKey("cashier.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<TransactionPayment(payment_type='{self.payment_type}', payment_total='{self.payment_total}')>"
