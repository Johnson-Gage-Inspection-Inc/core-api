from pydantic import BaseModel, StrictStr as StrictStr

class QualerApiModelsAddressAddressModel(BaseModel):
    first_name: StrictStr | None
    last_name: StrictStr | None
    email: StrictStr | None
    company: StrictStr | None
    city: StrictStr | None
    address1: StrictStr | None
    address2: StrictStr | None
    zip_postal_code: StrictStr | None
    phone_number: StrictStr | None
    fax_number: StrictStr | None
    attention1: StrictStr | None
    attention2: StrictStr | None
    country: StrictStr | None
    state_province: StrictStr | None
    state_province_abbreviation: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsAddressAddressModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsAddressAddressModel: ...
