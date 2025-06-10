from pydantic import BaseModel, StrictFloat as StrictFloat, StrictInt as StrictInt

class QualerApiModelsEmployeesFromEmployeeLocationModel(BaseModel):
    latitude: StrictFloat | StrictInt | None
    longitude: StrictFloat | StrictInt | None
    accuracy: StrictFloat | StrictInt | None
    altitude: StrictFloat | StrictInt | None
    altitude_accuracy: StrictFloat | StrictInt | None
    heading: StrictFloat | StrictInt | None
    speed: StrictFloat | StrictInt | None
    timestamp: StrictInt | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsEmployeesFromEmployeeLocationModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsEmployeesFromEmployeeLocationModel: ...
