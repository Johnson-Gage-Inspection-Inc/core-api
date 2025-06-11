from datetime import datetime
from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerApiModelsAssetToAssetManageResponseModel(BaseModel):
    asset_id: StrictInt | None
    asset_name: StrictStr | None
    asset_description: StrictStr | None
    asset_maker: StrictStr | None
    record_type: StrictInt | None
    parent_asset_id: StrictInt | None
    children_count: StrictInt | None
    site_id: StrictInt | None
    serial_number: StrictStr | None
    asset_tag: StrictStr | None
    asset_user: StrictStr | None
    equipment_id: StrictStr | None
    legacy_identifier: StrictStr | None
    criticality: StrictStr | None
    condition: StrictStr | None
    asset_class: StrictStr | None
    activation_date: datetime | None
    retirment_date: datetime | None
    client_vendor_id: StrictInt | None
    company_name: StrictStr | None
    site_name: StrictStr | None
    asset_has_image: StrictBool | None
    has_image: StrictBool | None
    parent_has_image: StrictBool | None
    pool_id: StrictInt | None
    pool: StrictStr | None
    product_id: StrictInt | None
    parent_product_id: StrictInt | None
    product_name: StrictStr | None
    parent_product_name: StrictStr | None
    category_id: StrictInt | None
    root_category_id: StrictInt | None
    category_name: StrictStr | None
    root_category_name: StrictStr | None
    manufacturer_id: StrictInt | None
    manufacturer: StrictStr | None
    display_part_number: StrictStr | None
    display_name: StrictStr | None
    manufacturer_part_number: StrictStr | None
    asset_room: StrictStr | None
    location: StrictStr | None
    station: StrictStr | None
    tool_role: StrictStr | None
    tool_id: StrictInt | None
    department_id: StrictInt | None
    department_name: StrictStr | None
    custodian_name: StrictStr | None
    warranty: StrictStr | None
    warranty_end: datetime | None
    is_warranty_expired: StrictBool | None
    depreciation_method: StrictInt | None
    depreciation_basis: StrictFloat | StrictInt | None
    salvage_value: StrictFloat | StrictInt | None
    total_service_cost: StrictFloat | StrictInt | None
    life_span_months: StrictInt | None
    due_for_replacement_date: datetime | None
    depreciation_proc: StrictFloat | StrictInt | None
    purchase_date: datetime | None
    purchase_cost: StrictFloat | StrictInt | None
    time_in_service: StrictInt | None
    retirement_reason: StrictStr | None
    residual_cost: StrictFloat | StrictInt | None
    employee_id: StrictInt | None
    asset_service_record_id: StrictInt | None
    result_status: StrictStr | None
    as_found_result: StrictStr | None
    as_left_result: StrictStr | None
    last_service_date: datetime | None
    last_service: StrictStr | None
    next_service_date: datetime | None
    next_service: StrictStr | None
    service_schedule_segment_id: StrictInt | None
    service_schedule_id: StrictInt | None
    service_schedule: StrictStr | None
    service_order_id: StrictInt | None
    service_order_status: StrictStr | None
    custom_order_number: StrictStr | None
    service_order_item_id: StrictInt | None
    vendor: StrictStr | None
    technician: StrictStr | None
    certificate_number: StrictStr | None
    due_trigger_date: datetime | None
    past_due_trigger_date: datetime | None
    due_status: StrictStr | None
    work_status: StrictStr | None
    def record_type_validate_enum(cls, value): ...
    def tool_role_validate_enum(cls, value): ...
    def result_status_validate_enum(cls, value): ...
    def as_found_result_validate_enum(cls, value): ...
    def as_left_result_validate_enum(cls, value): ...
    def service_order_status_validate_enum(cls, value): ...
    def due_status_validate_enum(cls, value): ...
    def work_status_validate_enum(cls, value): ...

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsAssetToAssetManageResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsAssetToAssetManageResponseModel: ...
