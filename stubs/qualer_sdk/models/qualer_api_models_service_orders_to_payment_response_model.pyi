from pydantic import BaseModel, StrictFloat as StrictFloat, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsServiceOrdersToPaymentResponseModel(BaseModel):
    service_order_id: StrictInt | None
    created_by_id: StrictInt | None
    transaction_id: StrictStr | None
    transaction_status: StrictStr | None
    payment_type: StrictStr | None
    service_order_payment_id: StrictInt | None
    payment_amount: StrictFloat | StrictInt | None
    details: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsServiceOrdersToPaymentResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsServiceOrdersToPaymentResponseModel: ...
