from pydantic import BaseModel, StrictStr as StrictStr

class QualerApiModelsClientsFromClientAssetQuery(BaseModel):
    equipment_id: StrictStr | None
    serial_number: StrictStr | None
    asset_tag: StrictStr | None
    barcode: StrictStr | None
    legacy_id: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsClientsFromClientAssetQuery: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsClientsFromClientAssetQuery: ...
