from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
    conlist as conlist,
)
from qualer_sdk.models.qualer_api_models_measurements_from_update_measurement_set_model import (
    QualerApiModelsMeasurementsFromUpdateMeasurementSetModel as QualerApiModelsMeasurementsFromUpdateMeasurementSetModel,
)

class QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel(BaseModel):
    batch_id: StrictInt | None
    batch_type: StrictStr | None
    save_and_delete_empty: StrictBool | None
    measurement_sets: None | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel: ...
