from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from pydantic import BaseModel as _BaseModel
from pydantic import Field as _Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0042JobResNodeCpus")


class V0042JobResNodeCpus(_BaseModel):
    """
    Attributes:
        count (int | Unset): Total number of CPUs assigned to job
        used (int | Unset): Total number of CPUs used by job
    """

    count: int | Unset = UNSET
    used: int | Unset = UNSET
    additional_properties: dict[str, Any] = _Field(init=False, default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        used = self.used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        used = d.pop("used", UNSET)

        v0042_job_res_node_cpus = cls(
            count=count,
            used=used,
        )

        v0042_job_res_node_cpus.additional_properties = d
        return v0042_job_res_node_cpus

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
