from datetime import datetime
from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel(BaseModel):
    service_order_task_id: StrictInt | None
    task_name: StrictStr | None
    task_details: StrictStr | None
    start_time: datetime | None
    finish_time: datetime | None
    time_spent_minutes: StrictInt | None
    price: StrictFloat | StrictInt | None
    is_hourly: StrictBool | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel: ...
