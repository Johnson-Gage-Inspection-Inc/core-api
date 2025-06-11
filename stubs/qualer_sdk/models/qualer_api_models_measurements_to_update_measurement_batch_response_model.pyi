from pydantic import (
    BaseModel,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
    conlist as conlist,
)
from qualer_sdk.models.qualer_api_models_measurements_to_update_measurement_set_response_model import (
    QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModel as QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModel,
)

class QualerApiModelsMeasurementsToUpdateMeasurementBatchResponseModel(BaseModel):
    batch_id: StrictInt | None
    batch_type: StrictStr | None
    measurement_sets: None | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsMeasurementsToUpdateMeasurementBatchResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsMeasurementsToUpdateMeasurementBatchResponseModel: ...
