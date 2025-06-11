from datetime import datetime
from pydantic import (
    BaseModel,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
    conlist as conlist,
)
from qualer_sdk.models.qualer_api_models_address_to_address_response_model import (
    QualerApiModelsAddressToAddressResponseModel as QualerApiModelsAddressToAddressResponseModel,
)
from qualer_sdk.models.qualer_api_models_attributes_to_attribute_response import (
    QualerApiModelsAttributesToAttributeResponse as QualerApiModelsAttributesToAttributeResponse,
)

class QualerApiModelsClientsToClientCompanyResponseModel(BaseModel):
    company_id: StrictInt | None
    account_number_text: StrictStr | None
    account_number: StrictInt | None
    currency_id: StrictInt | None
    client_status: StrictStr | None
    company_name: StrictStr | None
    company_description: StrictStr | None
    domain_name: StrictStr | None
    custom_client_name: StrictStr | None
    legacy_id: StrictStr | None
    updated_on_utc: datetime | None
    account_representative_employee_id: StrictInt | None
    account_representative_site_id: StrictInt | None
    account_manager_employee_id: StrictInt | None
    billing_address: QualerApiModelsAddressToAddressResponseModel | None
    shipping_address: QualerApiModelsAddressToAddressResponseModel | None
    attributes: None | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsClientsToClientCompanyResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsClientsToClientCompanyResponseModel: ...
