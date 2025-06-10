from datetime import datetime
from pydantic import BaseModel, StrictBool as StrictBool, StrictFloat as StrictFloat, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel(BaseModel):
    asset_id: StrictInt | None
    asset_service_record_id: StrictInt | None
    service_schedule_segment_id: StrictInt | None
    forward_segment_id: StrictInt | None
    forward_next_service: StrictBool | None
    service_order_number: StrictInt | None
    custom_order_number: StrictStr | None
    order_item_number: StrictInt | None
    certificate_number: StrictStr | None
    result_status: StrictStr | None
    as_found_result: StrictStr | None
    as_left_result: StrictStr | None
    service_date: datetime | None
    serial_number: StrictStr | None
    asset_tag: StrictStr | None
    asset_user: StrictStr | None
    asset_tag_change: StrictStr | None
    asset_user_change: StrictStr | None
    service_notes: StrictStr | None
    serial_number_change: StrictStr | None
    due_date: datetime | None
    next_service_date: datetime | None
    provider_technician: StrictStr | None
    provider_phone: StrictStr | None
    provider_company: StrictStr | None
    service_level: StrictStr | None
    service_level_code: StrictStr | None
    next_service_level: StrictStr | None
    next_service_level_code: StrictStr | None
    asset_name: StrictStr | None
    asset_description: StrictStr | None
    parts_charge: StrictFloat | StrictInt | None
    parts_charge_before_discount: StrictFloat | StrictInt | None
    service_charge: StrictFloat | StrictInt | None
    repairs_charge: StrictFloat | StrictInt | None
    guid: StrictStr | None
    segment_name: StrictStr | None
    schedule_name: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel: ...
