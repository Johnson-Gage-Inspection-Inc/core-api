from pydantic import BaseModel, StrictBool as StrictBool, StrictStr as StrictStr

class QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel(BaseModel):
    service_order_status: StrictStr | None
    reset_status: StrictBool | None
    email: StrictStr | None
    password: StrictStr | None
    def service_order_status_validate_enum(cls, value): ...

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel: ...
