from pydantic import BaseModel, StrictBool as StrictBool, StrictInt as StrictInt, StrictStr as StrictStr
from qualer_sdk.models.qualer_api_models_address_address_model import QualerApiModelsAddressAddressModel as QualerApiModelsAddressAddressModel

class QualerApiModelsSiteFromSiteUpdateModel(BaseModel):
    site_id: StrictInt | None
    site_name: StrictStr | None
    site_code: StrictStr | None
    shipping_inherited: StrictBool | None
    default_account_representative_employee_id: StrictInt | None
    billing_inherited: StrictBool | None
    federal_number: StrictStr | None
    state_number: StrictStr | None
    culture_name: StrictStr | None
    is_science_facility: StrictBool | None
    is_service_center: StrictBool | None
    is_inventory_storage: StrictBool | None
    is_production: StrictBool | None
    time_zone_id: StrictStr | None
    time_zone_offset_minutes: StrictInt | None
    company_name: StrictStr | None
    billing_address: QualerApiModelsAddressAddressModel | None
    shipping_address: QualerApiModelsAddressAddressModel | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsSiteFromSiteUpdateModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsSiteFromSiteUpdateModel: ...
