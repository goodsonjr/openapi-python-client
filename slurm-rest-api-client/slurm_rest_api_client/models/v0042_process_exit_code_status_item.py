from enum import StrEnum, auto


class V0042ProcessExitCodeStatusItem(StrEnum):
    CORE_DUMPED = auto()
    ERROR = auto()
    INVALID = auto()
    PENDING = auto()
    SIGNALED = auto()
    SUCCESS = auto()
