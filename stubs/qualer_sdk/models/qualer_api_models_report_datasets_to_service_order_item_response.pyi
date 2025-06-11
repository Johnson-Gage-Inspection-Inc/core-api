from datetime import datetime
from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerApiModelsReportDatasetsToServiceOrderItemResponse(BaseModel):
    certificate_number: StrictStr | None
    document_number: StrictStr | None
    revision: StrictStr | None
    effective_date: datetime | None
    document_section: StrictStr | None
    service_level: StrictStr | None
    service_level_code: StrictStr | None
    service_type: StrictStr | None
    order_item_number: StrictInt | None
    service_charge: StrictFloat | StrictInt | None
    updated_by: StrictStr | None
    updated_on: datetime | None
    work_status: StrictInt | None
    custom_work_status: StrictStr | None
    service_comments: StrictStr | None
    client_notes: StrictStr | None
    vendor_service_notes: StrictStr | None
    display_name: StrictStr | None
    display_part_number: StrictStr | None
    part_number: StrictStr | None
    schedule_name: StrictStr | None
    segment_name: StrictStr | None
    next_segment_name: StrictStr | None
    interval_length: StrictInt | None
    interval_cycle: StrictStr | None
    service_options: StrictStr | None
    service_options_price: StrictStr | None
    service_options_document_numbers: StrictStr | None
    location: StrictStr | None
    station: StrictStr | None
    room: StrictStr | None
    site: StrictStr | None
    vendor_id: StrictInt | None
    service_order_number: StrictInt | None
    custom_order_number: StrictStr | None
    linked_order_number: StrictStr | None
    asset_id: StrictInt | None
    asset_class: StrictStr | None
    asset_condition: StrictStr | None
    asset_criticality: StrictStr | None
    asset_pool: StrictStr | None
    asset_name: StrictStr | None
    asset_description: StrictStr | None
    asset_document_number: StrictStr | None
    asset_document_section: StrictStr | None
    document_number_values: StrictStr | None
    product_name: StrictStr | None
    product_description: StrictStr | None
    asset_maker: StrictStr | None
    category_name: StrictStr | None
    root_category_name: StrictStr | None
    vendor_tag: StrictStr | None
    result_status: StrictInt | None
    service_date: datetime | None
    next_service_date: datetime | None
    original_due_date: datetime | None
    asset_tag: StrictStr | None
    department: StrictStr | None
    asset_user: StrictStr | None
    equipment_id: StrictStr | None
    legacy_identifier: StrictStr | None
    activation_date: datetime | None
    purchase_date: datetime | None
    part_name: StrictStr | None
    part_description: StrictStr | None
    is_taxable: StrictBool | None
    is_limited: StrictBool | None
    quantity: StrictFloat | StrictInt | None
    discount: StrictFloat | StrictInt | None
    price: StrictFloat | StrictInt | None
    time_spent_in_minutes: StrictFloat | StrictInt | None
    is_hourly_pricing: StrictBool | None
    delivery_charge: StrictFloat | StrictInt | None
    serial_number: StrictStr | None
    part_repair_charges: StrictFloat | StrictInt | None
    part_repair_price: StrictFloat | StrictInt | None
    override_parts_total: StrictBool | None
    override_repairs_total: StrictBool | None
    asset_custodian_name: StrictStr | None
    as_found_specification_group_name: StrictStr | None
    as_found_specification_company_name: StrictStr | None
    as_left_specification_group_name: StrictStr | None
    as_left_specification_company_name: StrictStr | None
    order_id: StrictInt | None
    parent_order_id: StrictInt | None
    order_item_id: StrictInt | None
    order_item_part_id: StrictInt | None
    as_found_specification_group_id: StrictInt | None
    as_left_specification_group_id: StrictInt | None
    as_found_status: StrictInt | None
    as_left_status: StrictInt | None
    as_found_result: StrictInt | None
    as_left_result: StrictInt | None
    completed_on: datetime | None
    received_on: datetime | None
    completed_by_name: StrictStr | None
    service_charge_base: StrictFloat | StrictInt | None
    service_total: StrictFloat | StrictInt | None
    repairs_total: StrictFloat | StrictInt | None
    parts_total: StrictFloat | StrictInt | None
    parts_total_before_discount: StrictFloat | StrictInt | None
    parent_manufacturer: StrictStr | None
    parent_location: StrictStr | None
    parent_manufacturer_part_number: StrictStr | None
    parent_display_part_number: StrictStr | None
    parent_asset_id: StrictInt | None
    parent_category_name: StrictStr | None
    parent_root_category_name: StrictStr | None
    parent_serial_number: StrictStr | None
    parent_asset_tag: StrictStr | None
    parent_asset_user: StrictStr | None
    parent_display_name: StrictStr | None
    parent_equipment_id: StrictStr | None
    asset_shipping_address1: StrictStr | None
    asset_shipping_address2: StrictStr | None
    asset_shipping_first_name: StrictStr | None
    asset_shipping_last_name: StrictStr | None
    asset_shipping_email: StrictStr | None
    asset_shipping_company: StrictStr | None
    asset_shipping_city: StrictStr | None
    asset_shipping_zip: StrictStr | None
    asset_shipping_phone_number: StrictStr | None
    asset_shipping_fax_number: StrictStr | None
    asset_shipping_country: StrictStr | None
    asset_shipping_state: StrictStr | None
    shipping_address1: StrictStr | None
    shipping_address2: StrictStr | None
    shipping_first_name: StrictStr | None
    shipping_last_name: StrictStr | None
    shipping_email: StrictStr | None
    shipping_company: StrictStr | None
    shipping_city: StrictStr | None
    shipping_zip: StrictStr | None
    shipping_phone_number: StrictStr | None
    shipping_fax_number: StrictStr | None
    shipping_country: StrictStr | None
    shipping_state: StrictStr | None
    asset_service_notes: StrictStr | None
    service_option_service_code: StrictStr | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsReportDatasetsToServiceOrderItemResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsReportDatasetsToServiceOrderItemResponse: ...
