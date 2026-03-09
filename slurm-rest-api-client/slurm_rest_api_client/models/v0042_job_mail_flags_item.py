from enum import StrEnum, auto


class V0042JobMailFlagsItem(StrEnum):
    ARRAY_TASKS = auto()
    BEGIN = auto()
    END = auto()
    FAIL = auto()
    INVALID_DEPENDENCY = auto()
    REQUEUE = auto()
    STAGE_OUT = auto()
    TIME100 = auto()
    TIME50 = auto()
    TIME80 = auto()
    TIME90 = auto()
