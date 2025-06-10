from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel(BaseModel):
    service_order_item_id: StrictInt | None
    task_name: StrictStr | None
    task_description: StrictStr | None
    as_found_details: StrictStr | None
    as_left_details: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel: ...
