from enum import StrEnum, auto


class V0042CpuBindingFlagsItem(StrEnum):
    CPU_BIND_LDMAP = auto()
    CPU_BIND_LDMASK = auto()
    CPU_BIND_LDRANK = auto()
    CPU_BIND_MAP = auto()
    CPU_BIND_MASK = auto()
    CPU_BIND_NONE = auto()
    CPU_BIND_ONE_THREAD_PER_CORE = auto()
    CPU_BIND_RANK = auto()
    CPU_BIND_TO_CORES = auto()
    CPU_BIND_TO_LDOMS = auto()
    CPU_BIND_TO_SOCKETS = auto()
    CPU_BIND_TO_THREADS = auto()
    VERBOSE = auto()
