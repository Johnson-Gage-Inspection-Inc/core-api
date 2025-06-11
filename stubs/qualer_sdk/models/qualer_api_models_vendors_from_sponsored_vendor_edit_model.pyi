from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr
from qualer_sdk.models.qualer_api_models_address_address_model import (
    QualerApiModelsAddressAddressModel as QualerApiModelsAddressAddressModel,
)

class QualerApiModelsVendorsFromSponsoredVendorEditModel(BaseModel):
    company_id: StrictInt | None
    account_number_text: StrictStr | None
    domain_name: StrictStr | None
    custom_vendor_name: StrictStr | None
    currency_id: StrictInt | None
    company_name: StrictStr | None
    billing_address: QualerApiModelsAddressAddressModel | None
    shipping_address: QualerApiModelsAddressAddressModel | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsVendorsFromSponsoredVendorEditModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsVendorsFromSponsoredVendorEditModel: ...
