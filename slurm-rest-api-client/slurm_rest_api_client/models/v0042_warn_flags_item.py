from enum import StrEnum, auto


class V0042WarnFlagsItem(StrEnum):
    ARRAY_TASK = auto()
    BATCH_JOB = auto()
    CRON_JOBS = auto()
    FEDERATION_REQUEUE = auto()
    FULL_JOB = auto()
    FULL_STEPS_ONLY = auto()
    HURRY = auto()
    NO_SIBLING_JOBS = auto()
    OUT_OF_MEMORY = auto()
    RESERVATION_JOB = auto()
    VERBOSE = auto()
    WARNING_SENT = auto()
