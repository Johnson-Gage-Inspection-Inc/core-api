from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel(BaseModel):
    service_order_item_part_id: StrictInt | None
    service_order_item_id: StrictInt | None
    name: StrictStr | None
    description: StrictStr | None
    discount: StrictFloat | StrictInt | None
    is_taxable: StrictBool | None
    is_hourly_pricing: StrictBool | None
    price: StrictFloat | StrictInt | None
    unit_name: StrictStr | None
    quantity: StrictFloat | StrictInt | None
    delivery_charge: StrictFloat | StrictInt | None
    time_spent_in_minutes: StrictFloat | StrictInt | None
    free_quantity: StrictInt | None
    service_order_charge_type: StrictStr | None
    def service_order_charge_type_validate_enum(cls, value): ...

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel: ...
