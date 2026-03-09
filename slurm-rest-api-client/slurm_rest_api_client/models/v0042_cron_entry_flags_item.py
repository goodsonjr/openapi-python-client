from enum import StrEnum, auto


class V0042CronEntryFlagsItem(StrEnum):
    WILD_DAY_OF_MONTH = auto()
    WILD_DAY_OF_WEEK = auto()
    WILD_HOUR = auto()
    WILD_MINUTE = auto()
    WILD_MONTH = auto()
