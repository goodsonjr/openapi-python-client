from enum import StrEnum, auto


class V0042CrTypeItem(StrEnum):
    BOARD = auto()
    CORE = auto()
    CORE_DEFAULT_DIST_BLOCK = auto()
    CPU = auto()
    LINEAR = auto()
    LLN = auto()
    MEMORY = auto()
    ONE_TASK_PER_CORE = auto()
    PACK_NODES = auto()
    SOCKET = auto()
