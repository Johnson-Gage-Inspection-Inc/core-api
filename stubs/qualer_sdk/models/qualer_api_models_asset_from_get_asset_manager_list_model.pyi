from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsAssetFromGetAssetManagerListModel(BaseModel):
    filter_type: StrictStr | None
    search_string: StrictStr | None
    page: StrictInt | None
    page_size: StrictInt | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsAssetFromGetAssetManagerListModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsAssetFromGetAssetManagerListModel: ...
