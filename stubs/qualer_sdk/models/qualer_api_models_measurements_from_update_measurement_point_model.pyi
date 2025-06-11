from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
    conlist as conlist,
)
from qualer_sdk.models.qualer_api_models_measurements_from_update_measurement_condition_factor_model import (
    QualerApiModelsMeasurementsFromUpdateMeasurementConditionFactorModel as QualerApiModelsMeasurementsFromUpdateMeasurementConditionFactorModel,
)
from qualer_sdk.models.qualer_api_models_measurements_from_update_measurement_model import (
    QualerApiModelsMeasurementsFromUpdateMeasurementModel as QualerApiModelsMeasurementsFromUpdateMeasurementModel,
)
from qualer_sdk.models.qualer_api_models_measurements_from_update_measurement_tool_model import (
    QualerApiModelsMeasurementsFromUpdateMeasurementToolModel as QualerApiModelsMeasurementsFromUpdateMeasurementToolModel,
)

class QualerApiModelsMeasurementsFromUpdateMeasurementPointModel(BaseModel):
    measurement_point_id: StrictInt | None
    specification_name: StrictStr | None
    unit_of_measure: StrictStr | None
    expected_value: StrictFloat | StrictInt | None
    expected_value_raw: StrictStr | None
    base_value: StrictFloat | StrictInt | None
    test_value: StrictFloat | StrictInt | None
    nominal: StrictFloat | StrictInt | None
    range_min: StrictFloat | StrictInt | None
    range_max: StrictFloat | StrictInt | None
    tolerance_type: StrictStr | None
    precision_type: StrictStr | None
    precision: StrictFloat | StrictInt | None
    tolerance_minimum: StrictFloat | StrictInt | None
    tolerance_maximum: StrictFloat | StrictInt | None
    resolution: StrictFloat | StrictInt | None
    resolution_count: StrictFloat | StrictInt | None
    is_accredited: StrictBool | None
    specification_mode: StrictStr | None
    tolerance_mode: StrictStr | None
    tolerance_unit: StrictStr | None
    measurements: None | None
    measurement_condition_factors: None | None
    tool_application_mode: StrictStr | None
    primary_measurement_tool: (
        QualerApiModelsMeasurementsFromUpdateMeasurementToolModel | None
    )
    secondary_measurement_tool: (
        QualerApiModelsMeasurementsFromUpdateMeasurementToolModel | None
    )
    linked_measurement_point_id: StrictInt | None
    hysteresis_point: StrictStr | None
    influence_parameter1_parameter_id: StrictInt | None
    influence_parameter1_value: StrictStr | None
    influence_parameter2_parameter_id: StrictInt | None
    influence_parameter2_value: StrictStr | None
    measurement_not_taken_reason: StrictStr | None
    hide_from_certificate: StrictBool | None
    measurement_not_taken_result: StrictStr | None
    is_measurement_not_taken: StrictBool | None
    column_mean: StrictStr | None
    column_mean_result: StrictStr | None
    column_sd: StrictStr | None
    column_sd_result: StrictStr | None
    column_cv: StrictStr | None
    column_cv_result: StrictStr | None
    column_range: StrictStr | None
    column_range_result: StrictStr | None
    column_delta: StrictStr | None
    column_delta_result: StrictStr | None
    column_result: StrictStr | None
    def specification_mode_validate_enum(cls, value): ...
    def tolerance_mode_validate_enum(cls, value): ...
    def tolerance_unit_validate_enum(cls, value): ...
    def tool_application_mode_validate_enum(cls, value): ...
    def hysteresis_point_validate_enum(cls, value): ...

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsMeasurementsFromUpdateMeasurementPointModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsMeasurementsFromUpdateMeasurementPointModel: ...
