from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr, conlist as conlist
from qualer_sdk.models.qualer_api_models_service_orders_to_base_work_item_model_order_item_task_price_model import QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel as QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel
from qualer_sdk.models.qualer_api_models_service_orders_to_base_work_item_model_order_part_repair_price_model import QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel as QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel

class QualerApiModelsServiceOrdersToBaseWorkItemModel(BaseModel):
    tasks: None | None
    parts: None | None
    repairs: None | None
    work_item_id: StrictInt | None
    vendor_tag: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsServiceOrdersToBaseWorkItemModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsServiceOrdersToBaseWorkItemModel: ...
