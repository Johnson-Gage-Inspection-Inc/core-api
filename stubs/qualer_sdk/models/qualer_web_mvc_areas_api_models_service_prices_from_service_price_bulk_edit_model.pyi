from pydantic import BaseModel, StrictBool as StrictBool, StrictFloat as StrictFloat, StrictInt as StrictInt, StrictStr as StrictStr

class QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel(BaseModel):
    service_option_id: StrictInt | None
    service_option: StrictStr | None
    service_option_code: StrictStr | None
    option_type: StrictStr | None
    description: StrictStr | None
    service_task_id: StrictInt | None
    service_code: StrictStr | None
    document_number: StrictStr | None
    document_section: StrictStr | None
    capability_id: StrictInt | None
    service_type_id: StrictInt | None
    service_task_price_id: StrictInt | None
    service_pricing_id: StrictInt | None
    price: StrictFloat | StrictInt | None
    is_hourly: StrictBool | None
    issue: StrictStr | None
    log_error: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel: ...
