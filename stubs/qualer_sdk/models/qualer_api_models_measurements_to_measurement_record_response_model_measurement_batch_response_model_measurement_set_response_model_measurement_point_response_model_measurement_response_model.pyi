from datetime import datetime
from pydantic import (
    BaseModel,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementResponseModel(
    BaseModel
):
    values: StrictStr | None
    mean: StrictFloat | StrictInt | None
    sd: StrictFloat | StrictInt | None
    range: StrictFloat | StrictInt | None
    delta: StrictFloat | StrictInt | None
    cv: StrictFloat | StrictInt | None
    cmc: StrictFloat | StrictInt | None
    mu: StrictFloat | StrictInt | None
    tur: StrictFloat | StrictInt | None
    tar: StrictFloat | StrictInt | None
    max_value: StrictFloat | StrictInt | None
    min_value: StrictFloat | StrictInt | None
    error: StrictFloat | StrictInt | None
    result: StrictStr | None
    updated_on: datetime | None
    updated_by: StrictStr | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementResponseModel: ...
