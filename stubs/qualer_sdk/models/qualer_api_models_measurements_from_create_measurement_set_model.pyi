from pydantic import BaseModel, StrictBool as StrictBool, StrictInt as StrictInt, StrictStr as StrictStr, conlist as conlist
from qualer_sdk.models.qualer_api_models_measurements_from_create_measurement_point_model import QualerApiModelsMeasurementsFromCreateMeasurementPointModel as QualerApiModelsMeasurementsFromCreateMeasurementPointModel
from qualer_sdk.models.qualer_api_models_measurements_from_custom_fields import QualerApiModelsMeasurementsFromCustomFields as QualerApiModelsMeasurementsFromCustomFields
from qualer_sdk.models.qualer_api_models_measurements_from_display_options import QualerApiModelsMeasurementsFromDisplayOptions as QualerApiModelsMeasurementsFromDisplayOptions

class QualerApiModelsMeasurementsFromCreateMeasurementSetModel(BaseModel):
    measurement_name: StrictStr | None
    is_accredited: StrictBool | None
    measurement_quantity_id: StrictInt | None
    default_unit_of_measure_id: StrictInt | None
    decimal_places: StrictInt | None
    significant_figures: StrictInt | None
    display_options: QualerApiModelsMeasurementsFromDisplayOptions | None
    custom_fields: QualerApiModelsMeasurementsFromCustomFields | None
    measurement_points: None | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsMeasurementsFromCreateMeasurementSetModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsMeasurementsFromCreateMeasurementSetModel: ...
