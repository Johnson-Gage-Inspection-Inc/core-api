from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsReportDatasetsToMeasurementFieldResponse(BaseModel):
    field_id: StrictStr | None
    name: StrictStr | None
    value: StrictStr | None
    measurement_name: StrictStr | None
    measurement_set_id: StrictInt | None
    specification_name: StrictStr | None
    measurement_point_id: StrictInt | None
    batch_type: StrictStr | None
    service_order_item_id: StrictInt | None
    service_order_id: StrictInt | None
    batch_field_id: StrictStr | None
    point_field_id: StrictStr | None
    def batch_type_validate_enum(cls, value): ...

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsReportDatasetsToMeasurementFieldResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsReportDatasetsToMeasurementFieldResponse: ...
