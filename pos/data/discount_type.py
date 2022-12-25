from enum import Enum, auto


class DiscountType(Enum):
    NONE = auto()
    PERSONAL = auto()
    MANAGER = auto()
    CUSTOMER_SATISFACTION = auto()
    PRODUCT = auto()

