from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerApiModelsServiceOptionsToServiceOptionResponseModel(BaseModel):
    name: StrictStr | None
    price: StrictFloat | StrictInt | None
    service_charge: StrictFloat | StrictInt | None
    time_spent: StrictFloat | StrictInt | None
    is_hourly: StrictBool | None
    document_number: StrictStr | None
    document_section: StrictStr | None
    service_code: StrictStr | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsServiceOptionsToServiceOptionResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsServiceOptionsToServiceOptionResponseModel: ...
