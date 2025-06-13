from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qualer_api_models_service_orders_to_base_work_item_model import (
    QualerApiModelsServiceOrdersToBaseWorkItemModel as QualerApiModelsServiceOrdersToBaseWorkItemModel,
)
from ..models.qualer_api_models_service_orders_to_charge_response_model_base_order_part_repair_price_model import (
    QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel as QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel,
)
from ..models.qualer_api_models_service_orders_to_charge_response_model_base_order_task_price_model import (
    QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel as QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel,
)
from ..models.qualer_api_models_service_orders_to_charge_response_model_base_price_model import (
    QualerApiModelsServiceOrdersToChargeResponseModelBasePriceModel as QualerApiModelsServiceOrdersToChargeResponseModelBasePriceModel,
)
from ..types import UNSET as UNSET
from ..types import Unset as Unset

T = TypeVar("T", bound="QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel")

@_attrs_define
class QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel:
    charges: (
        Unset | list["QualerApiModelsServiceOrdersToChargeResponseModelBasePriceModel"]
    ) = ...
    tasks: (
        Unset
        | list[
            "QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel"
        ]
    ) = ...
    parts: (
        Unset
        | list[
            "QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel"
        ]
    ) = ...
    repairs: (
        Unset
        | list[
            "QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel"
        ]
    ) = ...
    work_items: Unset | list["QualerApiModelsServiceOrdersToBaseWorkItemModel"] = ...
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
