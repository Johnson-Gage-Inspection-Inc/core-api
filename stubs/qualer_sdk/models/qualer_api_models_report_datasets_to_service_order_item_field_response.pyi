from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse(BaseModel):
    field_id: StrictStr | None
    type: StrictStr | None
    value: StrictStr | None
    service_order_item_id: StrictInt | None
    service_order_item_task_id: StrictInt | None
    def type_validate_enum(cls, value): ...

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse: ...
