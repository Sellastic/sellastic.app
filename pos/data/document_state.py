from enum import Enum, auto


class DocumentState(Enum):
    NONE = auto()
    CLOSED = auto()
    SUSPENDED = auto()
    OPENED = auto()
