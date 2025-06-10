from pydantic import BaseModel, StrictBool as StrictBool, StrictInt as StrictInt, StrictStr as StrictStr, conlist as conlist
from qualer_sdk.models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_custom_fields import QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields as QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields
from qualer_sdk.models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_display_options import QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelDisplayOptions as QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelDisplayOptions
from qualer_sdk.models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model_measurement_point_response_model import QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModel as QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModel

class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel(BaseModel):
    measurement_name: StrictStr | None
    is_accredited: StrictBool | None
    measurement_quantity_id: StrictInt | None
    default_unit_of_measure_id: StrictInt | None
    decimal_places: StrictInt | None
    significant_figures: StrictInt | None
    display_options: QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelDisplayOptions | None
    custom_fields: QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields | None
    measurement_points: None | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel: ...
