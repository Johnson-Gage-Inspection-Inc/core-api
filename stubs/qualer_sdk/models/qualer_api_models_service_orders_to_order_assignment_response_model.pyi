from datetime import datetime
from pydantic import BaseModel, StrictBool as StrictBool, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsServiceOrdersToOrderAssignmentResponseModel(BaseModel):
    work_item_id: StrictInt | None
    employee_id: StrictInt | None
    company_id: StrictInt | None
    subscription_email: StrictStr | None
    subscription_phone: StrictStr | None
    office_phone: StrictStr | None
    is_locked: StrictBool | None
    image_url: StrictStr | None
    alias: StrictStr | None
    title: StrictStr | None
    is_deleted: StrictBool | None
    last_seen_date_utc: datetime | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsServiceOrdersToOrderAssignmentResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsServiceOrdersToOrderAssignmentResponseModel: ...
