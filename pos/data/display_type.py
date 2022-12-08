from enum import Enum, auto


class DisplayType(Enum):
    NONE = auto()
    LOGIN = auto()
    MENU = auto()
    SALE = auto()
    SERVICE = auto()
    SETTING = auto()
    PARAMETER = auto()
    REPORT = auto()
    FUNCTION = auto()
    CUSTOMER = auto()
    VOID = auto()
    REFUND = auto()
    STOCK = auto()
    END_OF_DAY = auto()
