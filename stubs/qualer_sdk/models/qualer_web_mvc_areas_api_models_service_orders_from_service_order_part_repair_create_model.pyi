from datetime import datetime
from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel(
    BaseModel
):
    name: StrictStr | None
    description: StrictStr | None
    charge_date: datetime | None
    price: StrictFloat | StrictInt | None
    unit_name: StrictStr | None
    is_hourly_pricing: StrictBool | None
    time_spent_in_minutes: StrictFloat | StrictInt | None
    quantity: StrictFloat | StrictInt | None
    discount: StrictFloat | StrictInt | None
    is_taxable: StrictBool | None
    delivery_charge: StrictFloat | StrictInt | None
    free_quantity: StrictInt | None
    created_by_id: StrictInt | None
    service_order_charge_type: StrictStr | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> (
        QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel
    ): ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> (
        QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel
    ): ...
