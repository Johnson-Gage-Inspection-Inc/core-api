from datetime import datetime
from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
    conbytes as conbytes,
    constr as constr,
)

class QualerApiModelsReportDatasetsToAssetSummaryResponse(BaseModel):
    service_order_number: StrictInt | None
    service_order_id: StrictInt | None
    service_order_item_id: StrictInt | None
    custom_order_number: StrictStr | None
    order_item_number: StrictInt | None
    is_limited: StrictBool | None
    certificate_number: StrictStr | None
    serial_number: StrictStr | None
    next_service_date: datetime | None
    service_date: datetime | None
    part_number: StrictStr | None
    display_part_number: StrictStr | None
    asset_tag: StrictStr | None
    asset_user: StrictStr | None
    asset_name: StrictStr | None
    equipment_id: StrictStr | None
    legacy_identifier: StrictStr | None
    asset_description: StrictStr | None
    var_class: StrictStr | None
    condition: StrictStr | None
    criticality: StrictStr | None
    asset_pool: StrictStr | None
    room: StrictStr | None
    station: StrictStr | None
    service_notes: StrictStr | None
    service_level: StrictStr | None
    service_level_code: StrictStr | None
    next_service_level: StrictStr | None
    next_service_level_code: StrictStr | None
    asset_id: StrictInt | None
    result_status: StrictInt | None
    serial_number_change: StrictStr | None
    provider_technician: StrictStr | None
    provider_technician_alias: StrictStr | None
    provider_phone: StrictStr | None
    provider_company: StrictStr | None
    qr_code: None | None | None
    bar_code: None | None | None
    bar_code_string: StrictStr | None
    owner_company_id: StrictInt | None
    owner_company_name: StrictStr | None
    as_found_result: StrictInt | None
    as_left_result: StrictInt | None
    asset_tag_change: StrictStr | None
    asset_user_change: StrictStr | None
    due_date: datetime | None
    parts_charge: StrictFloat | StrictInt | None
    parts_charge_before_discount: StrictFloat | StrictInt | None
    service_charge: StrictFloat | StrictInt | None
    repairs_charge: StrictFloat | StrictInt | None
    segment_name: StrictStr | None
    schedule_name: StrictStr | None
    next_segment_name: StrictStr | None
    client_id: StrictInt | None
    interval_length: StrictInt | None
    interval_cycle: StrictStr | None
    def qr_code_validate_regular_expression(cls, value): ...
    def bar_code_validate_regular_expression(cls, value): ...

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsReportDatasetsToAssetSummaryResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsReportDatasetsToAssetSummaryResponse: ...
