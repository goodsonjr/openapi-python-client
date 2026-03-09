from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from pydantic import BaseModel as _BaseModel
from pydantic import Field as _Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0042PartitionInfoTres")


class V0042PartitionInfoTres(_BaseModel):
    """
    Attributes:
        billing_weights (str | Unset): TRESBillingWeights
        configured (str | Unset): TRES
    """

    billing_weights: str | Unset = UNSET
    configured: str | Unset = UNSET
    additional_properties: dict[str, Any] = _Field(init=False, default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_weights = self.billing_weights

        configured = self.configured

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_weights is not UNSET:
            field_dict["billing_weights"] = billing_weights
        if configured is not UNSET:
            field_dict["configured"] = configured

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        billing_weights = d.pop("billing_weights", UNSET)

        configured = d.pop("configured", UNSET)

        v0042_partition_info_tres = cls(
            billing_weights=billing_weights,
            configured=configured,
        )

        v0042_partition_info_tres.additional_properties = d
        return v0042_partition_info_tres

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
