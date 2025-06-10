from pydantic import BaseModel, StrictBool as StrictBool, StrictFloat as StrictFloat, StrictInt as StrictInt, StrictStr as StrictStr, conlist as conlist
from qualer_sdk.models.qualer_api_models_measurements_from_create_measurement_condition_factor_model import QualerApiModelsMeasurementsFromCreateMeasurementConditionFactorModel as QualerApiModelsMeasurementsFromCreateMeasurementConditionFactorModel
from qualer_sdk.models.qualer_api_models_measurements_from_create_measurement_model import QualerApiModelsMeasurementsFromCreateMeasurementModel as QualerApiModelsMeasurementsFromCreateMeasurementModel
from qualer_sdk.models.qualer_api_models_measurements_from_create_measurement_tool_model import QualerApiModelsMeasurementsFromCreateMeasurementToolModel as QualerApiModelsMeasurementsFromCreateMeasurementToolModel

class QualerApiModelsMeasurementsFromCreateMeasurementPointModel(BaseModel):
    specification_name: StrictStr | None
    measurement_quantity: StrictStr | None
    unit_of_measure_id: StrictInt | None
    unit_of_measure: StrictStr | None
    range_min: StrictFloat | StrictInt | None
    range_max: StrictFloat | StrictInt | None
    specification_mode: StrictStr | None
    tolerance_type: StrictStr | None
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
    primary_measurement_tool: QualerApiModelsMeasurementsFromCreateMeasurementToolModel | None
    secondary_measurement_tool: QualerApiModelsMeasurementsFromCreateMeasurementToolModel | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsMeasurementsFromCreateMeasurementPointModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsMeasurementsFromCreateMeasurementPointModel: ...
