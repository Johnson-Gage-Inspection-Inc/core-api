from datetime import datetime
from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsVendorsFromVendorCompanySearchModel(BaseModel):
    account_number_text: StrictStr | None
    company_name: StrictStr | None
    take: StrictInt | None
    modified_after: datetime | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsVendorsFromVendorCompanySearchModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsVendorsFromVendorCompanySearchModel: ...
