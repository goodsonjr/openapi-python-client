from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from pydantic import BaseModel as _BaseModel
from pydantic import Field as _Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0042PartitionInfoCpus")


class V0042PartitionInfoCpus(_BaseModel):
    """
    Attributes:
        task_binding (int | Unset): CpuBind
        total (int | Unset): TotalCPUs
    """

    task_binding: int | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _Field(init=False, default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_binding = self.task_binding

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_binding is not UNSET:
            field_dict["task_binding"] = task_binding
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_binding = d.pop("task_binding", UNSET)

        total = d.pop("total", UNSET)

        v0042_partition_info_cpus = cls(
            task_binding=task_binding,
            total=total,
        )

        v0042_partition_info_cpus.additional_properties = d
        return v0042_partition_info_cpus

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
