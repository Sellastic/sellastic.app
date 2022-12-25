from sqlalchemy import Column, Integer, BigInteger, Boolean, String, DateTime, Float, ForeignKey, UUID
from sqlalchemy.sql import func

from data_layer.model.crud_model import Model
from data_layer.model.crud_model import CRUD

from uuid import uuid4


class TransactionHeadTemp(Model, CRUD):
    def __init__(self):
        Model.__init__(self)
        CRUD.__init__(self)

    __tablename__ = "transaction_head_temp"

    id = Column(BigInteger, primary_key=True, autoincrement=True, default=1)
    transaction_unique_id = Column(String(50), nullable=False, default=uuid4())
    pos_id = Column(Integer, nullable=False)
    transaction_date_time = Column(DateTime, server_default=func.now(), nullable=False)
    document_type = Column(String(50), nullable=False)
    fk_customer_id = Column(BigInteger, ForeignKey("customer.id"))
    receipt_number = Column(Integer, nullable=False)
    batch_number = Column(Integer, nullable=False)
    total_amount = Column(Integer, nullable=False)
    total_vat_amount = Column(Integer, nullable=False)
    total_discount_amount = Column(Integer, nullable=False)
    total_surcharge_amount = Column(Integer, nullable=False)
    total_payment_amount = Column(Integer, nullable=False)
    total_change_amount = Column(Integer, nullable=False)
    description = Column(String(100))
    is_closed = Column(Boolean, nullable=False)
    is_pending = Column(Boolean, nullable=False)
    is_cancel = Column(Boolean, nullable=False)
    is_deleted = Column(Boolean, nullable=False)
    delete_description = Column(String(1000), nullable=True)
    fk_cashier_create_id = Column(BigInteger, ForeignKey("cashier.id"))
    fk_cashier_update_id = Column(BigInteger, ForeignKey("cashier.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<TransactionHeadTemp(transaction_unique_id='{self.transaction_unique_id}', transaction_date_time='{self.transaction_date_time}')>"
