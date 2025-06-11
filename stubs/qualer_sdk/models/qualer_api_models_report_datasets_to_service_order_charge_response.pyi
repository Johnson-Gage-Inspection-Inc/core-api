from datetime import datetime
from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerApiModelsReportDatasetsToServiceOrderChargeResponse(BaseModel):
    service_order_id: StrictInt | None
    description: StrictStr | None
    name: StrictStr | None
    unit_name: StrictStr | None
    quantity: StrictFloat | StrictInt | None
    discount: StrictFloat | StrictInt | None
    fixed_charge: StrictFloat | StrictInt | None
    price: StrictFloat | StrictInt | None
    subtotal: StrictFloat | StrictInt | None
    is_taxable: StrictBool | None
    time_spent_in_minutes: StrictFloat | StrictInt | None
    is_hourly_pricing: StrictBool | None
    created_by: StrictStr | None
    charge_date: datetime | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsReportDatasetsToServiceOrderChargeResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsReportDatasetsToServiceOrderChargeResponse: ...
