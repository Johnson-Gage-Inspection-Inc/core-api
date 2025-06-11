from datetime import datetime
from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerApiModelsReportDatasetsToServiceOrderItemStatusHistoryResponse(BaseModel):
    service_order_item_id: StrictInt | None
    previous_status_name: StrictStr | None
    selected_status_name: StrictStr | None
    explanation: StrictStr | None
    is_password_reentered: StrictBool | None
    created_on: datetime | None
    created_on_utc: datetime | None
    employee_id: StrictInt | None
    first_name: StrictStr | None
    last_name: StrictStr | None
    alias: StrictStr | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsReportDatasetsToServiceOrderItemStatusHistoryResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsReportDatasetsToServiceOrderItemStatusHistoryResponse: ...
