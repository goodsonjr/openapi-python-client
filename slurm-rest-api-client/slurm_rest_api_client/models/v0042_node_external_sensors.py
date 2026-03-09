from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from pydantic import BaseModel as _BaseModel
from pydantic import Field as _Field

T = TypeVar("T", bound="V0042NodeExternalSensors")


class V0042NodeExternalSensors(_BaseModel):
    """ """

    additional_properties: dict[str, Any] = _Field(init=False, default_factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        v0042_node_external_sensors = cls()

        v0042_node_external_sensors.additional_properties = d
        return v0042_node_external_sensors

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
