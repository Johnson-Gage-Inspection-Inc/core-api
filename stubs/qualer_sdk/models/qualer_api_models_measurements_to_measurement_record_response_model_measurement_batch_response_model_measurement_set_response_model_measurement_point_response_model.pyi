from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
    conlist as conlist,
)
from qualer_sdk.models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model_measurement_point_response_model_measurement_condition_factor_response_model import (
    QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementConditionFactorResponseModel as QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementConditionFactorResponseModel,
)
from qualer_sdk.models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model_measurement_point_response_model_measurement_response_model import (
    QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementResponseModel as QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementResponseModel,
)
from qualer_sdk.models.qualer_api_models_measurements_to_measurement_record_response_model_measurement_batch_response_model_measurement_set_response_model_measurement_point_response_model_measurement_tool_response_model import (
    QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementToolResponseModel as QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementToolResponseModel,
)

class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModel(
    BaseModel
):
    specification_name: StrictStr | None
    measurement_quantity: StrictStr | None
    unit_of_measure_id: StrictInt | None
    unit_of_measure: StrictStr | None
    range_min: StrictFloat | StrictInt | None
    range_max: StrictFloat | StrictInt | None
    tolerance_type: StrictStr | None
    specification_mode: StrictStr | None
    tolerance_mode: StrictStr | None
    tolerance_unit: StrictStr | None
    precision_type: StrictStr | None
    readings: StrictInt | None
    channels_type: StrictStr | None
    channel_count: StrictInt | None
    precision: StrictFloat | StrictInt | None
    tolerance_minimum: StrictFloat | StrictInt | None
    tolerance_maximum: StrictFloat | StrictInt | None
    resolution: StrictFloat | StrictInt | None
    resolution_count: StrictFloat | StrictInt | None
    nominal: StrictFloat | StrictInt | None
    expected_value: StrictFloat | StrictInt | None
    base_value: StrictFloat | StrictInt | None
    test_value: StrictFloat | StrictInt | None
    is_accredited: StrictBool | None
    measurements: None | None
    condition_factors: None | None
    primary_measurement_tool: (
        QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementToolResponseModel
        | None
    )
    secondary_measurement_tool: (
        QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementToolResponseModel
        | None
    )
    def specification_mode_validate_enum(cls, value): ...
    def tolerance_mode_validate_enum(cls, value): ...
    def tolerance_unit_validate_enum(cls, value): ...

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModel: ...
