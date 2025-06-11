from datetime import datetime
from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerApiModelsServiceOrdersToServiceOrderPartRepairResponse(BaseModel):
    service_order_item_part_id: StrictInt | None
    price: StrictFloat | StrictInt | None
    description: StrictStr | None
    name: StrictStr | None
    unit_name: StrictStr | None
    quantity: StrictFloat | StrictInt | None
    discount: StrictFloat | StrictInt | None
    delivery_charge: StrictFloat | StrictInt | None
    is_taxable: StrictBool | None
    time_spent_in_minutes: StrictFloat | StrictInt | None
    is_hourly_pricing: StrictBool | None
    free_quantity: StrictInt | None
    currency_iso_symbol: StrictStr | None
    created_by_id: StrictInt | None
    created_by: StrictStr | None
    created_on_utc: datetime | None
    charge_date: datetime | None
    contract_repairs_discount: StrictFloat | StrictInt | None
    contract_parts_discount: StrictFloat | StrictInt | None
    service_order_charge_type: StrictStr | None
    total_discount: StrictFloat | StrictInt | None
    total_price: StrictFloat | StrictInt | None
    discount_price: StrictFloat | StrictInt | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsServiceOrdersToServiceOrderPartRepairResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsServiceOrdersToServiceOrderPartRepairResponse: ...
