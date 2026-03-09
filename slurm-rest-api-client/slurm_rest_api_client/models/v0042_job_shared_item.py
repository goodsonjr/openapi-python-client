from enum import StrEnum, auto


class V0042JobSharedItem(StrEnum):
    MCS = auto()
    NONE = auto()
    OVERSUBSCRIBE = auto()
    TOPO = auto()
    USER = auto()
