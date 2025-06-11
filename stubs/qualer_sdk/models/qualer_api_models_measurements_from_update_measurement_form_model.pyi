from pydantic import BaseModel, conlist as conlist
from qualer_sdk.models.qualer_api_models_measurements_from_update_measurement_batch_model import (
    QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel as QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel,
)

class QualerApiModelsMeasurementsFromUpdateMeasurementFormModel(BaseModel):
    measurement_batches: None | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsMeasurementsFromUpdateMeasurementFormModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsMeasurementsFromUpdateMeasurementFormModel: ...
