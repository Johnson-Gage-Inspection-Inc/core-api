from pydantic import BaseModel, StrictStr as StrictStr

class QualerApiModelsReportDatasetsToServiceOrderAssigneeResponse(BaseModel):
    first_name: StrictStr | None
    last_name: StrictStr | None
    alias: StrictStr | None
    email: StrictStr | None
    title: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsReportDatasetsToServiceOrderAssigneeResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsReportDatasetsToServiceOrderAssigneeResponse: ...
