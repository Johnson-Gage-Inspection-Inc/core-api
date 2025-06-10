from datetime import datetime
from pydantic import BaseModel, StrictBool as StrictBool, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel(BaseModel):
    service_order_id: StrictInt | None
    guid: StrictStr | None
    service_order_number: StrictInt | None
    custom_order_number: StrictStr | None
    due_date: datetime | None
    assets: StrictInt | None
    completed_assets: StrictInt | None
    order_status: StrictStr | None
    is_quality_control_fail: StrictBool | None
    service_private_comments: StrictStr | None
    client_company_id: StrictInt | None
    client_company_name: StrictStr | None
    client_site_name: StrictStr | None
    client_legacy_id: StrictStr | None
    business_from_time: datetime | None
    business_to_time: datetime | None
    timeframe: StrictStr | None
    site_access_notes: StrictStr | None
    desired_date: datetime | None
    deadline_date: datetime | None
    request_from_date: datetime | None
    request_from_time: datetime | None
    request_to_date: datetime | None
    request_to_time: datetime | None
    def order_status_validate_enum(cls, value): ...
    def timeframe_validate_enum(cls, value): ...
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel: ...
