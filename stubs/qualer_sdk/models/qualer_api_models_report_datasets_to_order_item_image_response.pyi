from pydantic import (
    BaseModel,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
    conbytes as conbytes,
    constr as constr,
)

class QualerApiModelsReportDatasetsToOrderItemImageResponse(BaseModel):
    service_order_item_id: StrictInt | None
    image: None | None | None
    image_url: StrictStr | None
    def image_validate_regular_expression(cls, value): ...

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsReportDatasetsToOrderItemImageResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsReportDatasetsToOrderItemImageResponse: ...
