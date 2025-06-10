from datetime import datetime
from pydantic import BaseModel, StrictFloat as StrictFloat, StrictInt as StrictInt, StrictStr as StrictStr, conlist as conlist
from qualer_sdk.models.qualer_api_models_asset_to_asset_maintenance_plan_response import QualerApiModelsAssetToAssetMaintenancePlanResponse as QualerApiModelsAssetToAssetMaintenancePlanResponse

class QualerApiModelsAssetToAssetMaintenancePlanModel(BaseModel):
    maintenance_plans: None | None
    company_id: StrictInt | None
    asset_id: StrictInt | None
    serial_number: StrictStr | None
    asset_user: StrictStr | None
    asset_tag: StrictStr | None
    equipment_id: StrictStr | None
    asset_status: StrictStr | None
    asset_name: StrictStr | None
    asset_description: StrictStr | None
    asset_maker: StrictStr | None
    location: StrictStr | None
    room_number: StrictStr | None
    barcode: StrictStr | None
    legacy_identifier: StrictStr | None
    root_category_name: StrictStr | None
    category_name: StrictStr | None
    var_class: StrictStr | None
    custodian_email: StrictStr | None
    custodian_first_name: StrictStr | None
    custodian_last_name: StrictStr | None
    custodian_name: StrictStr | None
    department: StrictStr | None
    station: StrictStr | None
    notes: StrictStr | None
    document_number: StrictStr | None
    document_section: StrictStr | None
    cumulative_service_cost: StrictFloat | StrictInt | None
    product_id: StrictInt | None
    manufacturer_part_number: StrictStr | None
    product_name: StrictStr | None
    product_description: StrictStr | None
    product_manufacturer: StrictStr | None
    site_name: StrictStr | None
    site_id: StrictInt | None
    condition: StrictStr | None
    criticality: StrictStr | None
    pool: StrictStr | None
    purchase_date: datetime | None
    purchase_cost: StrictFloat | StrictInt | None
    life_span_months: StrictInt | None
    activation_date: datetime | None
    depreciation_basis: StrictFloat | StrictInt | None
    depreciation_method: StrictInt | None
    retirement_date: datetime | None
    salvage_value: StrictFloat | StrictInt | None
    retirment_reason: StrictStr | None
    composite_parent_id: StrictInt | None
    composite_child_count: StrictInt | None
    def asset_status_validate_enum(cls, value): ...
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsAssetToAssetMaintenancePlanModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsAssetToAssetMaintenancePlanModel: ...
