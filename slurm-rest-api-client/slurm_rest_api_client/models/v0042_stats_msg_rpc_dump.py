from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from pydantic import BaseModel as _BaseModel
from pydantic import Field as _Field

T = TypeVar("T", bound="V0042StatsMsgRpcDump")


class V0042StatsMsgRpcDump(_BaseModel):
    """
    Attributes:
        type_id (int): Message type as integer
        message_type (str): Message type as string
        count (list[str]):
    """

    type_id: int
    message_type: str
    count: list[str]
    additional_properties: dict[str, Any] = _Field(init=False, default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_id = self.type_id

        message_type = self.message_type

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type_id": type_id,
                "message_type": message_type,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_id = d.pop("type_id")

        message_type = d.pop("message_type")

        count = cast(list[str], d.pop("count"))

        v0042_stats_msg_rpc_dump = cls(
            type_id=type_id,
            message_type=message_type,
            count=count,
        )

        v0042_stats_msg_rpc_dump.additional_properties = d
        return v0042_stats_msg_rpc_dump

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
