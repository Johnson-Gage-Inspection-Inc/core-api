from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse(BaseModel):
    service_order_item_id: StrictInt | None
    measurement_point_id: StrictInt | None
    batch_type: StrictStr | None
    column_index: StrictInt | None
    mean: StrictStr | None
    mean_result: StrictBool | None
    sd: StrictStr | None
    sd_result: StrictBool | None
    cv: StrictStr | None
    cv_result: StrictBool | None
    range: StrictStr | None
    range_result: StrictBool | None
    delta: StrictStr | None
    delta_result: StrictBool | None
    result: StrictStr | None
    def batch_type_validate_enum(cls, value): ...
    def result_validate_enum(cls, value): ...

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse: ...
