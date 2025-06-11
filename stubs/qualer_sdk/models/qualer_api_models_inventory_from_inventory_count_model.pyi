from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerApiModelsInventoryFromInventoryCountModel(BaseModel):
    product_id: StrictInt | None
    manufacturer: StrictStr | None
    part_number: StrictStr | None
    is_stock_item: StrictBool | None
    quantity_on_hand: StrictInt | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsInventoryFromInventoryCountModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsInventoryFromInventoryCountModel: ...
