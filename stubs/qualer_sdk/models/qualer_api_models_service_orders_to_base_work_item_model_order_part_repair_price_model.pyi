from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel(
    BaseModel
):
    delivery_charge: StrictFloat | StrictInt | None
    quantity: StrictFloat | StrictInt | None
    time_spent_in_minutes: StrictFloat | StrictInt | None
    is_hourly_pricing: StrictBool | None
    description: StrictStr | None
    name: StrictStr | None
    price: StrictFloat | StrictInt | None
    unit_name: StrictStr | None
    is_taxable: StrictBool | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel: ...
