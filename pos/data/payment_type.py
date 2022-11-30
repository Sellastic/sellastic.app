from enum import Enum, auto


class PaymentType(Enum):
    NONE = auto()
    CASH = auto()
    CREDIT_CARD = auto()
    CHECK = auto()
    ON_CREDIT = auto()
    PREPAID_CARD = auto()
    MOBILE = auto()
    BONUS = auto()
    EXCHANGE = auto()
    CURRENT_ACCOUNT = auto()
    BANK_TRANSFER = auto()
