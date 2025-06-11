from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsClientsFromSponsoredEmployeeModel(BaseModel):
    client_company_id: StrictInt | None
    first_name: StrictStr | None
    last_name: StrictStr | None
    login_email: StrictStr | None
    password: StrictStr | None
    subscription_email: StrictStr | None
    mobile_phone: StrictStr | None
    office_phone: StrictStr | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsClientsFromSponsoredEmployeeModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsClientsFromSponsoredEmployeeModel: ...
