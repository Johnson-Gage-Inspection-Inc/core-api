from pydantic import BaseModel, StrictBool as StrictBool, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsReportDatasetsToMeasurementChannelResultResponse(BaseModel):
    service_order_item_id: StrictInt | None
    measurement_point_id: StrictInt | None
    column_index: StrictInt | None
    batch_type: StrictStr | None
    result: StrictStr | None
    mean_result: StrictBool | None
    range_result: StrictBool | None
    delta_result: StrictBool | None
    min_result: StrictBool | None
    max_result: StrictBool | None
    tar_result: StrictBool | None
    tur_result: StrictBool | None
    error_result: StrictBool | None
    sd_result: StrictBool | None
    cv_result: StrictBool | None
    def batch_type_validate_enum(cls, value): ...
    def result_validate_enum(cls, value): ...
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsReportDatasetsToMeasurementChannelResultResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsReportDatasetsToMeasurementChannelResultResponse: ...
