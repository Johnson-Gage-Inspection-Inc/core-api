from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr
from qualer_sdk.models.qualer_api_models_address_address_model import QualerApiModelsAddressAddressModel as QualerApiModelsAddressAddressModel

class QualerApiModelsClientsFromSponsoredClientCreateModel(BaseModel):
    account_number_text: StrictStr | None
    client_status: StrictStr | None
    domain_name: StrictStr | None
    custom_client_name: StrictStr | None
    legacy_id: StrictStr | None
    currency_id: StrictInt | None
    account_representative_employee_id: StrictInt | None
    account_representative_site_id: StrictInt | None
    account_manager_employee_id: StrictInt | None
    company_name: StrictStr | None
    billing_address: QualerApiModelsAddressAddressModel | None
    shipping_address: QualerApiModelsAddressAddressModel | None
    def client_status_validate_enum(cls, value): ...
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsClientsFromSponsoredClientCreateModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsClientsFromSponsoredClientCreateModel: ...
