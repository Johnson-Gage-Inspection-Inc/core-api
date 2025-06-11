from pydantic import BaseModel, StrictInt as StrictInt

class QualerApiModelsClientsFromClientEmployeeModel(BaseModel):
    employee_id: StrictInt | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsClientsFromClientEmployeeModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsClientsFromClientEmployeeModel: ...
