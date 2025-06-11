from datetime import datetime
from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsAccountToEmployeeEventResponseModel(BaseModel):
    id: StrictInt | None
    subject: StrictStr | None
    created_on_utc: datetime | None
    event_type_id: StrictInt | None
    event_type_group: StrictStr | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsAccountToEmployeeEventResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsAccountToEmployeeEventResponseModel: ...
