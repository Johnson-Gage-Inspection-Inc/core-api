from datetime import datetime
from pydantic import BaseModel, StrictBool as StrictBool, StrictFloat as StrictFloat, StrictInt as StrictInt, StrictStr as StrictStr, conlist as conlist
from qualer_sdk.models.qualer_api_models_service_options_to_service_option_response_model import QualerApiModelsServiceOptionsToServiceOptionResponseModel as QualerApiModelsServiceOptionsToServiceOptionResponseModel

class QualerApiModelsServiceOrdersToClientOrderItemResponseModel(BaseModel):
    work_item_id: StrictInt | None
    client_notes: StrictStr | None
    service_comments: StrictStr | None
    private_comments: StrictStr | None
    order_item_number: StrictInt | None
    service_order_id: StrictInt | None
    channel_count: StrictInt | None
    service_total: StrictFloat | StrictInt | None
    repairs_total: StrictFloat | StrictInt | None
    parts_total: StrictFloat | StrictInt | None
    parts_total_before_discount: StrictFloat | StrictInt | None
    override_service_total: StrictBool | None
    override_repairs_total: StrictBool | None
    override_parts_total: StrictBool | None
    service_type: StrictStr | None
    document_number: StrictStr | None
    document_section: StrictStr | None
    work_status: StrictStr | None
    custom_work_status: StrictStr | None
    is_limited: StrictBool | None
    checked_on: datetime | None
    checked_by_name: StrictStr | None
    checked_by_id: StrictInt | None
    completed_on: datetime | None
    completed_by_name: StrictStr | None
    completed_by_id: StrictInt | None
    updated_by_id: StrictInt | None
    updated_by: StrictStr | None
    as_found_check: StrictStr | None
    as_left_check: StrictStr | None
    item_result_status: StrictStr | None
    item_as_found_result: StrictStr | None
    item_as_left_result: StrictStr | None
    as_found_specification: StrictInt | None
    as_left_specification: StrictInt | None
    created_on_utc: datetime | None
    updated_on_utc: datetime | None
    equipment_id: StrictStr | None
    service_level: StrictStr | None
    service_level_code: StrictStr | None
    service_level_document_number: StrictStr | None
    service_level_document_section: StrictStr | None
    next_service_level: StrictStr | None
    next_service_level_code: StrictStr | None
    result_status: StrictStr | None
    as_found_result: StrictStr | None
    as_left_result: StrictStr | None
    serial_number: StrictStr | None
    serial_number_change: StrictStr | None
    asset_tag: StrictStr | None
    asset_user: StrictStr | None
    asset_tag_change: StrictStr | None
    asset_user_change: StrictStr | None
    asset_id: StrictInt | None
    asset_name: StrictStr | None
    asset_description: StrictStr | None
    asset_site_name: StrictStr | None
    asset_site_id: StrictInt | None
    asset_company_name: StrictStr | None
    asset_company_id: StrictInt | None
    client_company_id: StrictInt | None
    vendor_company_id: StrictInt | None
    service_notes: StrictStr | None
    provider_technician: StrictStr | None
    provider_phone: StrictStr | None
    provider_company: StrictStr | None
    service_charge: StrictFloat | StrictInt | None
    repairs_charge: StrictFloat | StrictInt | None
    parts_charge: StrictFloat | StrictInt | None
    parts_charge_before_discount: StrictFloat | StrictInt | None
    custom_order_number: StrictStr | None
    certificate_number: StrictStr | None
    service_date: datetime | None
    due_date: datetime | None
    next_service_date: datetime | None
    maintenance_task: StrictStr | None
    maintenance_plan: StrictStr | None
    service_options: None | None
    vendor_tag: StrictStr | None
    legacy_id: StrictStr | None
    asset_ownership: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsServiceOrdersToClientOrderItemResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsServiceOrdersToClientOrderItemResponseModel: ...
