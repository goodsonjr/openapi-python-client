from enum import StrEnum, auto


class GetNodeFlags(StrEnum):
    ALL = auto()
    DETAIL = auto()
    FEDERATION = auto()
    FUTURE = auto()
    LOCAL = auto()
    MIXED = auto()
    SIBLING = auto()
