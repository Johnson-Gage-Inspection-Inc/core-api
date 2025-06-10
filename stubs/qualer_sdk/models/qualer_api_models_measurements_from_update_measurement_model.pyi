from datetime import datetime
from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsMeasurementsFromUpdateMeasurementModel(BaseModel):
    measurement_id: StrictInt | None
    values: StrictStr | None
    channel: StrictInt | None
    updated_by: StrictStr | None
    updated_on: datetime | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsMeasurementsFromUpdateMeasurementModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsMeasurementsFromUpdateMeasurementModel: ...
