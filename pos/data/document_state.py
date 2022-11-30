from enum import Enum, auto


class DocumentState(Enum):
    CLOSED = auto()
    SUSPENDED = auto()
    OPENED = auto()
