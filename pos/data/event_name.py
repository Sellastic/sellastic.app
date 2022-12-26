from enum import Enum, auto


class EventName(Enum):
    NONE = auto()
    EXIT_APPLICATION = auto()
    LOGIN = auto()
    LOGOUT = auto()
    SALE = auto()
    CLOSURE = auto()
    CONFIG = auto()
    BACK = auto()
