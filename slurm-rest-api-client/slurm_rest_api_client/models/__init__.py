"""Contains all the data models used in inputs/outputs"""

from .delete_job_flags import DeleteJobFlags
from .get_job_flags import GetJobFlags
from .get_jobs_flags import GetJobsFlags
from .get_node_flags import GetNodeFlags
from .get_nodes_flags import GetNodesFlags
from .get_partition_flags import GetPartitionFlags
from .get_partitions_flags import GetPartitionsFlags
from .v0042_acct_gather_energy import V0042AcctGatherEnergy
from .v0042_acct_gather_profile_item import V0042AcctGatherProfileItem
from .v0042_assoc_shares_obj_wrap import V0042AssocSharesObjWrap
from .v0042_assoc_shares_obj_wrap_fairshare import V0042AssocSharesObjWrapFairshare
from .v0042_assoc_shares_obj_wrap_tres import V0042AssocSharesObjWrapTres
from .v0042_assoc_shares_obj_wrap_type_item import V0042AssocSharesObjWrapTypeItem
from .v0042_bf_exit_fields import V0042BfExitFields
from .v0042_controller_ping import V0042ControllerPing
from .v0042_cpu_binding_flags_item import V0042CpuBindingFlagsItem
from .v0042_cr_type_item import V0042CrTypeItem
from .v0042_cron_entry import V0042CronEntry
from .v0042_cron_entry_flags_item import V0042CronEntryFlagsItem
from .v0042_cron_entry_line import V0042CronEntryLine
from .v0042_float_64_no_val_struct import V0042Float64NoValStruct
from .v0042_job_alloc_req import V0042JobAllocReq
from .v0042_job_array_response_msg_entry import V0042JobArrayResponseMsgEntry
from .v0042_job_desc_msg import V0042JobDescMsg
from .v0042_job_desc_msg_rlimits import V0042JobDescMsgRlimits
from .v0042_job_flags_item import V0042JobFlagsItem
from .v0042_job_info import V0042JobInfo
from .v0042_job_info_job_resources_type_0 import V0042JobInfoJobResourcesType0
from .v0042_job_info_job_resources_type_0_nodes import V0042JobInfoJobResourcesType0Nodes
from .v0042_job_info_power import V0042JobInfoPower
from .v0042_job_mail_flags_item import V0042JobMailFlagsItem
from .v0042_job_res_core import V0042JobResCore
from .v0042_job_res_core_status_item import V0042JobResCoreStatusItem
from .v0042_job_res_node import V0042JobResNode
from .v0042_job_res_node_cpus import V0042JobResNodeCpus
from .v0042_job_res_node_memory import V0042JobResNodeMemory
from .v0042_job_res_socket import V0042JobResSocket
from .v0042_job_shared_item import V0042JobSharedItem
from .v0042_job_state_item import V0042JobStateItem
from .v0042_job_submit_req import V0042JobSubmitReq
from .v0042_kill_jobs_msg import V0042KillJobsMsg
from .v0042_kill_jobs_resp_job import V0042KillJobsRespJob
from .v0042_kill_jobs_resp_job_error import V0042KillJobsRespJobError
from .v0042_kill_jobs_resp_job_federation import V0042KillJobsRespJobFederation
from .v0042_license import V0042License
from .v0042_memory_binding_type_item import V0042MemoryBindingTypeItem
from .v0042_node import V0042Node
from .v0042_node_cr_type_item import V0042NodeCrTypeItem
from .v0042_node_external_sensors import V0042NodeExternalSensors
from .v0042_node_power import V0042NodePower
from .v0042_node_states_item import V0042NodeStatesItem
from .v0042_open_mode_item import V0042OpenModeItem
from .v0042_openapi_diag_resp import V0042OpenapiDiagResp
from .v0042_openapi_error import V0042OpenapiError
from .v0042_openapi_job_alloc_resp import V0042OpenapiJobAllocResp
from .v0042_openapi_job_info_resp import V0042OpenapiJobInfoResp
from .v0042_openapi_job_post_response import V0042OpenapiJobPostResponse
from .v0042_openapi_job_submit_response import V0042OpenapiJobSubmitResponse
from .v0042_openapi_kill_job_resp import V0042OpenapiKillJobResp
from .v0042_openapi_kill_jobs_resp import V0042OpenapiKillJobsResp
from .v0042_openapi_licenses_resp import V0042OpenapiLicensesResp
from .v0042_openapi_meta import V0042OpenapiMeta
from .v0042_openapi_meta_client import V0042OpenapiMetaClient
from .v0042_openapi_meta_plugin import V0042OpenapiMetaPlugin
from .v0042_openapi_meta_slurm import V0042OpenapiMetaSlurm
from .v0042_openapi_meta_slurm_version import V0042OpenapiMetaSlurmVersion
from .v0042_openapi_nodes_resp import V0042OpenapiNodesResp
from .v0042_openapi_partition_resp import V0042OpenapiPartitionResp
from .v0042_openapi_ping_array_resp import V0042OpenapiPingArrayResp
from .v0042_openapi_reservation_resp import V0042OpenapiReservationResp
from .v0042_openapi_resp import V0042OpenapiResp
from .v0042_openapi_shares_resp import V0042OpenapiSharesResp
from .v0042_openapi_warning import V0042OpenapiWarning
from .v0042_oversubscribe_flags_item import V0042OversubscribeFlagsItem
from .v0042_part_prio import V0042PartPrio
from .v0042_partition_info import V0042PartitionInfo
from .v0042_partition_info_accounts import V0042PartitionInfoAccounts
from .v0042_partition_info_cpus import V0042PartitionInfoCpus
from .v0042_partition_info_defaults import V0042PartitionInfoDefaults
from .v0042_partition_info_groups import V0042PartitionInfoGroups
from .v0042_partition_info_maximums import V0042PartitionInfoMaximums
from .v0042_partition_info_maximums_oversubscribe import V0042PartitionInfoMaximumsOversubscribe
from .v0042_partition_info_minimums import V0042PartitionInfoMinimums
from .v0042_partition_info_nodes import V0042PartitionInfoNodes
from .v0042_partition_info_partition import V0042PartitionInfoPartition
from .v0042_partition_info_priority import V0042PartitionInfoPriority
from .v0042_partition_info_qos import V0042PartitionInfoQos
from .v0042_partition_info_timeouts import V0042PartitionInfoTimeouts
from .v0042_partition_info_tres import V0042PartitionInfoTres
from .v0042_partition_states_item import V0042PartitionStatesItem
from .v0042_process_exit_code_status_item import V0042ProcessExitCodeStatusItem
from .v0042_process_exit_code_verbose import V0042ProcessExitCodeVerbose
from .v0042_process_exit_code_verbose_signal import V0042ProcessExitCodeVerboseSignal
from .v0042_reservation_core_spec import V0042ReservationCoreSpec
from .v0042_reservation_flags_item import V0042ReservationFlagsItem
from .v0042_reservation_info import V0042ReservationInfo
from .v0042_reservation_info_purge_completed import V0042ReservationInfoPurgeCompleted
from .v0042_schedule_exit_fields import V0042ScheduleExitFields
from .v0042_shares_float_128_tres import V0042SharesFloat128Tres
from .v0042_shares_resp_msg import V0042SharesRespMsg
from .v0042_shares_uint_64_tres import V0042SharesUint64Tres
from .v0042_stats_msg import V0042StatsMsg
from .v0042_stats_msg_rpc_dump import V0042StatsMsgRpcDump
from .v0042_stats_msg_rpc_queue import V0042StatsMsgRpcQueue
from .v0042_stats_msg_rpc_type import V0042StatsMsgRpcType
from .v0042_stats_msg_rpc_user import V0042StatsMsgRpcUser
from .v0042_uint_16_no_val_struct import V0042Uint16NoValStruct
from .v0042_uint_32_no_val_struct import V0042Uint32NoValStruct
from .v0042_uint_64_no_val_struct import V0042Uint64NoValStruct
from .v0042_update_node_msg import V0042UpdateNodeMsg
from .v0042_warn_flags_item import V0042WarnFlagsItem
from .v0042x11_flags_item import V0042X11FlagsItem

__all__ = (
    "DeleteJobFlags",
    "GetJobFlags",
    "GetJobsFlags",
    "GetNodeFlags",
    "GetNodesFlags",
    "GetPartitionFlags",
    "GetPartitionsFlags",
    "V0042AcctGatherEnergy",
    "V0042AcctGatherProfileItem",
    "V0042AssocSharesObjWrap",
    "V0042AssocSharesObjWrapFairshare",
    "V0042AssocSharesObjWrapTres",
    "V0042AssocSharesObjWrapTypeItem",
    "V0042BfExitFields",
    "V0042ControllerPing",
    "V0042CpuBindingFlagsItem",
    "V0042CronEntry",
    "V0042CronEntryFlagsItem",
    "V0042CronEntryLine",
    "V0042CrTypeItem",
    "V0042Float64NoValStruct",
    "V0042JobAllocReq",
    "V0042JobArrayResponseMsgEntry",
    "V0042JobDescMsg",
    "V0042JobDescMsgRlimits",
    "V0042JobFlagsItem",
    "V0042JobInfo",
    "V0042JobInfoJobResourcesType0",
    "V0042JobInfoJobResourcesType0Nodes",
    "V0042JobInfoPower",
    "V0042JobMailFlagsItem",
    "V0042JobResCore",
    "V0042JobResCoreStatusItem",
    "V0042JobResNode",
    "V0042JobResNodeCpus",
    "V0042JobResNodeMemory",
    "V0042JobResSocket",
    "V0042JobSharedItem",
    "V0042JobStateItem",
    "V0042JobSubmitReq",
    "V0042KillJobsMsg",
    "V0042KillJobsRespJob",
    "V0042KillJobsRespJobError",
    "V0042KillJobsRespJobFederation",
    "V0042License",
    "V0042MemoryBindingTypeItem",
    "V0042Node",
    "V0042NodeCrTypeItem",
    "V0042NodeExternalSensors",
    "V0042NodePower",
    "V0042NodeStatesItem",
    "V0042OpenapiDiagResp",
    "V0042OpenapiError",
    "V0042OpenapiJobAllocResp",
    "V0042OpenapiJobInfoResp",
    "V0042OpenapiJobPostResponse",
    "V0042OpenapiJobSubmitResponse",
    "V0042OpenapiKillJobResp",
    "V0042OpenapiKillJobsResp",
    "V0042OpenapiLicensesResp",
    "V0042OpenapiMeta",
    "V0042OpenapiMetaClient",
    "V0042OpenapiMetaPlugin",
    "V0042OpenapiMetaSlurm",
    "V0042OpenapiMetaSlurmVersion",
    "V0042OpenapiNodesResp",
    "V0042OpenapiPartitionResp",
    "V0042OpenapiPingArrayResp",
    "V0042OpenapiReservationResp",
    "V0042OpenapiResp",
    "V0042OpenapiSharesResp",
    "V0042OpenapiWarning",
    "V0042OpenModeItem",
    "V0042OversubscribeFlagsItem",
    "V0042PartitionInfo",
    "V0042PartitionInfoAccounts",
    "V0042PartitionInfoCpus",
    "V0042PartitionInfoDefaults",
    "V0042PartitionInfoGroups",
    "V0042PartitionInfoMaximums",
    "V0042PartitionInfoMaximumsOversubscribe",
    "V0042PartitionInfoMinimums",
    "V0042PartitionInfoNodes",
    "V0042PartitionInfoPartition",
    "V0042PartitionInfoPriority",
    "V0042PartitionInfoQos",
    "V0042PartitionInfoTimeouts",
    "V0042PartitionInfoTres",
    "V0042PartitionStatesItem",
    "V0042PartPrio",
    "V0042ProcessExitCodeStatusItem",
    "V0042ProcessExitCodeVerbose",
    "V0042ProcessExitCodeVerboseSignal",
    "V0042ReservationCoreSpec",
    "V0042ReservationFlagsItem",
    "V0042ReservationInfo",
    "V0042ReservationInfoPurgeCompleted",
    "V0042ScheduleExitFields",
    "V0042SharesFloat128Tres",
    "V0042SharesRespMsg",
    "V0042SharesUint64Tres",
    "V0042StatsMsg",
    "V0042StatsMsgRpcDump",
    "V0042StatsMsgRpcQueue",
    "V0042StatsMsgRpcType",
    "V0042StatsMsgRpcUser",
    "V0042Uint16NoValStruct",
    "V0042Uint32NoValStruct",
    "V0042Uint64NoValStruct",
    "V0042UpdateNodeMsg",
    "V0042WarnFlagsItem",
    "V0042X11FlagsItem",
)
