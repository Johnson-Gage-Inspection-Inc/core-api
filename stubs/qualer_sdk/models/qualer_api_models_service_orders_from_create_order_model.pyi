from pydantic import BaseModel, StrictBool as StrictBool, StrictInt as StrictInt, StrictStr as StrictStr, conlist as conlist

class QualerApiModelsServiceOrdersFromCreateOrderModel(BaseModel):
    client_company_id: StrictInt | None
    vendor_site_id: StrictInt | None
    asset_ids: None | None
    schedule_segment_ids: None | None
    service_level_ids: None | None
    use_due_segments: StrictBool | None
    order_notes: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsServiceOrdersFromCreateOrderModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsServiceOrdersFromCreateOrderModel: ...
