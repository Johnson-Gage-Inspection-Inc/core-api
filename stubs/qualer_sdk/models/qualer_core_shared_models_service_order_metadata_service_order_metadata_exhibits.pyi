from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_core_shared_models_service_order_metadata_service_order_metadata_exhibits_key_value import (
    QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibitsKeyValue as QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibitsKeyValue,
)
from ..types import UNSET as UNSET
from ..types import Unset as Unset

T = TypeVar(
    "T", bound="QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits"
)

@_attrs_define
class QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits:
    title: Unset | str = ...
    subtitle: Unset | str = ...
    exhibits: (
        Unset
        | list[
            "QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibitsKeyValue"
        ]
    ) = ...
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)
    def to_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> T: ...
    @property
    def additional_keys(self) -> list[str]: ...
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __contains__(self, key: str) -> bool: ...
