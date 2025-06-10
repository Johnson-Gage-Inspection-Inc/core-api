from pydantic import BaseModel, StrictFloat as StrictFloat, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsMeasurementsToUpdateMeasurementConditionFactorResponse(BaseModel):
    measurement_condition_factor_id: StrictInt | None
    factor_id: StrictStr | None
    factor_name: StrictStr | None
    factor_value: StrictFloat | StrictInt | None
    factor_uom: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsMeasurementsToUpdateMeasurementConditionFactorResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsMeasurementsToUpdateMeasurementConditionFactorResponse: ...
