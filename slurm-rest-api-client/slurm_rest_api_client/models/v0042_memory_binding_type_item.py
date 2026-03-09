from enum import StrEnum, auto


class V0042MemoryBindingTypeItem(StrEnum):
    LOCAL = auto()
    MAP = auto()
    MASK = auto()
    NONE = auto()
    PREFER = auto()
    RANK = auto()
    SORT = auto()
    VERBOSE = auto()
