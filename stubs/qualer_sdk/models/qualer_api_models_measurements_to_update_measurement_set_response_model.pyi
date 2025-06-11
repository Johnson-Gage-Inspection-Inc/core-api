from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
    conlist as conlist,
)
from qualer_sdk.models.qualer_api_models_measurements_to_update_measurement_field_response_model import (
    QualerApiModelsMeasurementsToUpdateMeasurementFieldResponseModel as QualerApiModelsMeasurementsToUpdateMeasurementFieldResponseModel,
)
from qualer_sdk.models.qualer_api_models_measurements_to_update_measurement_point_response_model import (
    QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel as QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel,
)

class QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModel(BaseModel):
    measurement_set_id: StrictInt | None
    measurement_name: StrictStr | None
    is_accredited: StrictBool | None
    use_expected_value: StrictBool | None
    decimal_places: StrictInt | None
    significant_figures: StrictInt | None
    influence_parameter1_type: StrictStr | None
    influence_parameter1_tool_type_id: StrictInt | None
    influence_parameter1_parameter_id: StrictInt | None
    influence_parameter1_source: StrictStr | None
    influence_parameter1_value: StrictStr | None
    influence_parameter2_type: StrictStr | None
    influence_parameter2_tool_type_id: StrictInt | None
    influence_parameter2_parameter_id: StrictInt | None
    influence_parameter2_source: StrictStr | None
    influence_parameter2_value: StrictStr | None
    measurement_points: None | None
    measurement_fields: None | None
    def influence_parameter1_type_validate_enum(cls, value): ...
    def influence_parameter2_type_validate_enum(cls, value): ...

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsMeasurementsToUpdateMeasurementSetResponseModel: ...
