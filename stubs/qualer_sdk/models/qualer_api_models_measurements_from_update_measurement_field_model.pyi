from pydantic import BaseModel, StrictStr as StrictStr

class QualerApiModelsMeasurementsFromUpdateMeasurementFieldModel(BaseModel):
    field_id: StrictStr | None
    name: StrictStr | None
    type: StrictStr | None
    value: StrictStr | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsMeasurementsFromUpdateMeasurementFieldModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsMeasurementsFromUpdateMeasurementFieldModel: ...
