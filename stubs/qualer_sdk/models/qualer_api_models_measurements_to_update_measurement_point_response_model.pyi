from pydantic import BaseModel, StrictBool as StrictBool, StrictFloat as StrictFloat, StrictInt as StrictInt, StrictStr as StrictStr, conlist as conlist
from qualer_sdk.models.qualer_api_models_measurements_to_update_measurement_condition_factor_response import QualerApiModelsMeasurementsToUpdateMeasurementConditionFactorResponse as QualerApiModelsMeasurementsToUpdateMeasurementConditionFactorResponse
from qualer_sdk.models.qualer_api_models_measurements_to_update_measurement_response_model import QualerApiModelsMeasurementsToUpdateMeasurementResponseModel as QualerApiModelsMeasurementsToUpdateMeasurementResponseModel
from qualer_sdk.models.qualer_api_models_measurements_to_update_measurement_tool_response_model import QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel as QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel

class QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel(BaseModel):
    measurement_point_id: StrictInt | None
    specification_name: StrictStr | None
    unit_of_measure: StrictStr | None
    expected_value: StrictFloat | StrictInt | None
    base_value: StrictFloat | StrictInt | None
    test_value: StrictFloat | StrictInt | None
    nominal: StrictFloat | StrictInt | None
    range_min: StrictFloat | StrictInt | None
    range_max: StrictFloat | StrictInt | None
    tolerance_type: StrictStr | None
    tolerance_mode: StrictStr | None
    tolerance_unit: StrictStr | None
    precision_type: StrictStr | None
    precision: StrictFloat | StrictInt | None
    tolerance_minimum: StrictFloat | StrictInt | None
    tolerance_maximum: StrictFloat | StrictInt | None
    resolution: StrictFloat | StrictInt | None
    resolution_count: StrictFloat | StrictInt | None
    is_accredited: StrictBool | None
    linked_measurement_point_id: StrictInt | None
    hysteresis_point: StrictStr | None
    hide_from_certificate: StrictBool | None
    is_measurement_not_taken: StrictBool | None
    measurement_not_taken_result: StrictStr | None
    measurement_not_taken_reason: StrictStr | None
    influence_parameter1_parameter_id: StrictInt | None
    influence_parameter1_value: StrictStr | None
    influence_parameter2_parameter_id: StrictInt | None
    influence_parameter2_value: StrictStr | None
    measurements: None | None
    measurement_condition_factors: None | None
    primary_measurement_tool: QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel | None
    secondary_measurement_tool: QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel: ...
