from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_service_orders_to_base_work_item_model_order_item_task_price_model import (
    QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel as QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel,
)
from ..models.qualer_api_models_service_orders_to_base_work_item_model_order_part_repair_price_model import (
    QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel as QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel,
)
from ..types import UNSET as UNSET
from ..types import Unset as Unset

T = TypeVar("T", bound="QualerApiModelsServiceOrdersToBaseWorkItemModel")

@_attrs_define
class QualerApiModelsServiceOrdersToBaseWorkItemModel:
    tasks: (
        Unset
        | list["QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel"]
    ) = ...
    parts: (
        Unset
        | list[
            "QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel"
        ]
    ) = ...
    repairs: (
        Unset
        | list[
            "QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel"
        ]
    ) = ...
    work_item_id: Unset | int = ...
    vendor_tag: Unset | str = ...
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
