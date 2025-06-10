from pydantic import BaseModel, conlist as conlist
from qualer_sdk.models.qualer_api_models_service_orders_to_base_work_item_model import QualerApiModelsServiceOrdersToBaseWorkItemModel as QualerApiModelsServiceOrdersToBaseWorkItemModel
from qualer_sdk.models.qualer_api_models_service_orders_to_charge_response_model_base_order_part_repair_price_model import QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel as QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderPartRepairPriceModel
from qualer_sdk.models.qualer_api_models_service_orders_to_charge_response_model_base_order_task_price_model import QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel as QualerApiModelsServiceOrdersToChargeResponseModelBaseOrderTaskPriceModel
from qualer_sdk.models.qualer_api_models_service_orders_to_charge_response_model_base_price_model import QualerApiModelsServiceOrdersToChargeResponseModelBasePriceModel as QualerApiModelsServiceOrdersToChargeResponseModelBasePriceModel

class QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel(BaseModel):
    charges: None | None
    tasks: None | None
    parts: None | None
    repairs: None | None
    work_items: None | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel: ...
