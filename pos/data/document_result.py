from enum import Enum, auto


class DocumentResult(Enum):
    NONE = auto()
    SUCCEED = auto()
    CANCELED_BY_CASHIER = auto()
    CANCELED_BY_APPLICATION = auto()
    CANCELED_BY_APPLICATION_AFTER_POWER_ON = auto()
    CANCELED_BY_APPLICATION_BECAUSE_OF_HANGING = auto()
    SUSPENDED = auto()
