from pydantic import BaseModel, StrictStr as StrictStr, conlist as conlist
from qualer_sdk.models.qualer_api_models_measurements_from_create_measurement_set_model import (
    QualerApiModelsMeasurementsFromCreateMeasurementSetModel as QualerApiModelsMeasurementsFromCreateMeasurementSetModel,
)
from qualer_sdk.models.qualer_api_models_measurements_from_specification import (
    QualerApiModelsMeasurementsFromSpecification as QualerApiModelsMeasurementsFromSpecification,
)

class QualerApiModelsMeasurementsFromCreateMeasurementFormModel(BaseModel):
    batch_type: StrictStr | None
    batch_result: StrictStr | None
    specification: QualerApiModelsMeasurementsFromSpecification | None
    measurement_sets: None | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsMeasurementsFromCreateMeasurementFormModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsMeasurementsFromCreateMeasurementFormModel: ...
