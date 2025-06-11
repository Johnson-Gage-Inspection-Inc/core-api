from datetime import datetime
from pydantic import (
    BaseModel,
    StrictStr as StrictStr,
    conbytes as conbytes,
    constr as constr,
)

class QualerApiModelsReportDatasetsToCompanyCertificationResponse(BaseModel):
    logo: None | None | None
    initial_date: datetime | None
    certification_date: datetime | None
    expiration_date: datetime | None
    certification_name: StrictStr | None
    certificate_number: StrictStr | None
    certification_authority: StrictStr | None
    certification_standard: StrictStr | None
    def logo_validate_regular_expression(cls, value): ...

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsReportDatasetsToCompanyCertificationResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsReportDatasetsToCompanyCertificationResponse: ...
