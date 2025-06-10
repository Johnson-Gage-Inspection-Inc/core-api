from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr, conbytes as conbytes, constr as constr

class QualerApiModelsReportDatasetsToMeasurementChartResponse(BaseModel):
    service_order_item_id: StrictInt | None
    measurement_set_id: StrictInt | None
    chart_type: StrictInt | None
    chart_image: None | None | None
    nominal: StrictStr | None
    title: StrictStr | None
    unit_of_measure: StrictStr | None
    abbreviated_uom: StrictStr | None
    def chart_image_validate_regular_expression(cls, value): ...
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsReportDatasetsToMeasurementChartResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsReportDatasetsToMeasurementChartResponse: ...
