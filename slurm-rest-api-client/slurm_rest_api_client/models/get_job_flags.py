from enum import StrEnum, auto


class GetJobFlags(StrEnum):
    ALL = auto()
    DETAIL = auto()
    FEDERATION = auto()
    FUTURE = auto()
    LOCAL = auto()
    MIXED = auto()
    SIBLING = auto()
