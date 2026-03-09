from enum import StrEnum, auto


class GetNodesFlags(StrEnum):
    ALL = auto()
    DETAIL = auto()
    FEDERATION = auto()
    FUTURE = auto()
    LOCAL = auto()
    MIXED = auto()
    SIBLING = auto()
