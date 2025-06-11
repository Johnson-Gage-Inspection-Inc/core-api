from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerApiModelsReportDatasetsToServiceOrderItemOptionResponse(BaseModel):
    service_order_item_id: StrictInt | None
    service_charge: StrictFloat | StrictInt | None
    time_spent: StrictFloat | StrictInt | None
    is_hourly: StrictBool | None
    price: StrictFloat | StrictInt | None
    task_name: StrictStr | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsReportDatasetsToServiceOrderItemOptionResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsReportDatasetsToServiceOrderItemOptionResponse: ...
