from pydantic import BaseModel, StrictFloat as StrictFloat, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsEnvironmentToEnvironmentModel(BaseModel):
    room_name: StrictStr | None
    factor_id: StrictStr | None
    station_id: StrictInt | None
    factor_name: StrictStr | None
    factor_value: StrictFloat | StrictInt | None
    valid_range_min: StrictFloat | StrictInt | None
    valid_range_max: StrictFloat | StrictInt | None
    unit_of_measure: StrictStr | None
    def factor_id_validate_enum(cls, value): ...
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsEnvironmentToEnvironmentModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsEnvironmentToEnvironmentModel: ...
