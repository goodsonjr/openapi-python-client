from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from pydantic import BaseModel as _BaseModel
from pydantic import Field as _Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V0042OpenapiWarning")


class V0042OpenapiWarning(_BaseModel):
    """
    Attributes:
        description (str | Unset): Long form warning description
        source (str | Unset): Source of warning or where warning was first detected
    """

    description: str | Unset = UNSET
    source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _Field(init=False, default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        source = d.pop("source", UNSET)

        v0042_openapi_warning = cls(
            description=description,
            source=source,
        )

        v0042_openapi_warning.additional_properties = d
        return v0042_openapi_warning

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
