from enum import Enum, auto


class DocumentType(Enum):
    NONE = auto()
    FISCAL_RECEIPT = auto()
    ELECTRONIC_RECEIPT = auto()
    NONE_FISCAL_RECEIPT = auto()
    INVOICE = auto()
    ELECTRONIC_INVOICE = auto()
    ELECTRONIC_CORPORATE_INVOICE = auto()
    ELECTRONIC_INDIVIDUAL_INVOICE = auto()
    DIPLOMATIC_INVOICE = auto()
    WAYBILL = auto()
    POS_PAID_OUT = auto()
    POS_PAID_IN = auto()
    RETURN_SLIP = auto()
    EXPENSE_SLIP = auto()

