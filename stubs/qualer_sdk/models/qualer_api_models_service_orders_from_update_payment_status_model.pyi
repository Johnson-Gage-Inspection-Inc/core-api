from datetime import datetime
from pydantic import BaseModel, StrictStr as StrictStr

class QualerApiModelsServiceOrdersFromUpdatePaymentStatusModel(BaseModel):
    payment_status: StrictStr | None
    invoiced_on: datetime | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsServiceOrdersFromUpdatePaymentStatusModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsServiceOrdersFromUpdatePaymentStatusModel: ...
