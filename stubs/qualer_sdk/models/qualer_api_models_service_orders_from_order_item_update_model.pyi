from datetime import datetime
from pydantic import BaseModel, StrictBool as StrictBool, StrictFloat as StrictFloat, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsServiceOrdersFromOrderItemUpdateModel(BaseModel):
    service_comments: StrictStr | None
    private_comments: StrictStr | None
    service_notes: StrictStr | None
    service_total: StrictFloat | StrictInt | None
    repairs_total: StrictFloat | StrictInt | None
    parts_total: StrictFloat | StrictInt | None
    work_status: StrictStr | None
    custom_work_status: StrictStr | None
    is_limited: StrictBool | None
    checked_on: datetime | None
    checked_by_name: StrictStr | None
    completed_on: datetime | None
    completed_by_name: StrictStr | None
    as_found_check: StrictStr | None
    as_left_check: StrictStr | None
    result_status: StrictStr | None
    as_found_result: StrictStr | None
    as_left_result: StrictStr | None
    equipment_id: StrictStr | None
    legacy_id: StrictStr | None
    serial_number: StrictStr | None
    serial_number_change: StrictStr | None
    asset_tag: StrictStr | None
    asset_tag_change: StrictStr | None
    asset_user: StrictStr | None
    asset_user_change: StrictStr | None
    provider_technician: StrictStr | None
    provider_phone: StrictStr | None
    provider_company: StrictStr | None
    certificate_number: StrictStr | None
    service_date: datetime | None
    next_service_date: datetime | None
    vendor_tag: StrictStr | None
    def work_status_validate_enum(cls, value): ...
    def as_found_check_validate_enum(cls, value): ...
    def as_left_check_validate_enum(cls, value): ...
    def result_status_validate_enum(cls, value): ...
    def as_found_result_validate_enum(cls, value): ...
    def as_left_result_validate_enum(cls, value): ...
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsServiceOrdersFromOrderItemUpdateModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsServiceOrdersFromOrderItemUpdateModel: ...
