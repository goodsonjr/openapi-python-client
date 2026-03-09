from enum import StrEnum, auto


class V0042PartitionStatesItem(StrEnum):
    DOWN = auto()
    DRAIN = auto()
    INACTIVE = auto()
    UNKNOWN = auto()
    UP = auto()
