from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsReportDatasetsToToolRangeAttributeResponse(BaseModel):
    measurement_point_id: StrictInt | None
    service_order_item_id: StrictInt | None
    tool_id: StrictInt | None
    range_title: StrictStr | None
    range_subtitle: StrictStr | None
    attribute_name: StrictStr | None
    attribute_value: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsReportDatasetsToToolRangeAttributeResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsReportDatasetsToToolRangeAttributeResponse: ...
