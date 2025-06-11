from pydantic import BaseModel, conlist as conlist
from qualer_sdk.models.qualer_api_models_service_orders_from_item_charge_update_model_item_price_model import (
    QualerApiModelsServiceOrdersFromItemChargeUpdateModelItemPriceModel as QualerApiModelsServiceOrdersFromItemChargeUpdateModelItemPriceModel,
)

class QualerApiModelsServiceOrdersFromItemChargeUpdateModel(BaseModel):
    charges: None | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsServiceOrdersFromItemChargeUpdateModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsServiceOrdersFromItemChargeUpdateModel: ...
