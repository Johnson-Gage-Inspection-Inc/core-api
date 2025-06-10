from pydantic import BaseModel, StrictStr as StrictStr, conlist as conlist
from qualer_sdk.models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_custom_fields_create_measurement_field_response_model import QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFieldsCreateMeasurementFieldResponseModel as QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFieldsCreateMeasurementFieldResponseModel

class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields(BaseModel):
    description: StrictStr | None
    result: StrictStr | None
    items: None | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields: ...
