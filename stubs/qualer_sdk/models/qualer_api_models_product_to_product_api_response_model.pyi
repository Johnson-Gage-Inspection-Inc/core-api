from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerApiModelsProductToProductApiResponseModel(BaseModel):
    product_id: StrictInt | None
    parent_product_id: StrictInt | None
    category_id: StrictInt | None
    manufacturer_id: StrictInt | None
    manufacturer_name: StrictStr | None
    product_name: StrictStr | None
    parent_product_name: StrictStr | None
    manufacturer_part_number: StrictStr | None
    product_description: StrictStr | None
    is_family: StrictBool | None
    is_discontinued: StrictBool | None
    is_stock_item: StrictBool | None
    unit_sale_price: StrictFloat | StrictInt | None
    supplier_information: StrictStr | None
    quantity_on_hand: StrictInt | None
    product_code: StrictStr | None
    category_name: StrictStr | None
    parent_category_name: StrictStr | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsProductToProductApiResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsProductToProductApiResponseModel: ...
