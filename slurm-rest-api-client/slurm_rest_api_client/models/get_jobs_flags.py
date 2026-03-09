from enum import StrEnum, auto


class GetJobsFlags(StrEnum):
    ALL = auto()
    DETAIL = auto()
    FEDERATION = auto()
    FUTURE = auto()
    LOCAL = auto()
    MIXED = auto()
    SIBLING = auto()
