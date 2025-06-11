from datetime import datetime
from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr
from qualer_sdk.models.qualer_api_models_address_to_address_response_model import (
    QualerApiModelsAddressToAddressResponseModel as QualerApiModelsAddressToAddressResponseModel,
)

class QualerApiModelsVendorsToVendorCompanyResponseModel(BaseModel):
    account_number_text: StrictStr | None
    account_number: StrictInt | None
    currency_id: StrictInt | None
    company_id: StrictInt | None
    company_name: StrictStr | None
    domain_name: StrictStr | None
    custom_name: StrictStr | None
    billing_address: QualerApiModelsAddressToAddressResponseModel | None
    shipping_address: QualerApiModelsAddressToAddressResponseModel | None
    updated_on_utc: datetime | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsVendorsToVendorCompanyResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsVendorsToVendorCompanyResponseModel: ...
