from pydantic import BaseModel, StrictStr as StrictStr, conlist as conlist
from qualer_sdk.models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model import (
    QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel as QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel,
)
from qualer_sdk.models.qualer_api_models_measurements_to_measurement_record_response_model_specification_response_model import (
    QualerApiModelsMeasurementsToMeasurementRecordResponseModelSpecificationResponseModel as QualerApiModelsMeasurementsToMeasurementRecordResponseModelSpecificationResponseModel,
)

class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModel(
    BaseModel
):
    batch_type: StrictStr | None
    batch_result: StrictStr | None
    specification: (
        QualerApiModelsMeasurementsToMeasurementRecordResponseModelSpecificationResponseModel
        | None
    )
    measurement_sets: None | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModel: ...
