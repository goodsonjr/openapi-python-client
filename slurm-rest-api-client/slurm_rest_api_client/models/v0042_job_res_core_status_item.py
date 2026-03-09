from enum import StrEnum, auto


class V0042JobResCoreStatusItem(StrEnum):
    ALLOCATED = auto()
    INVALID = auto()
    IN_USE = auto()
    UNALLOCATED = auto()
