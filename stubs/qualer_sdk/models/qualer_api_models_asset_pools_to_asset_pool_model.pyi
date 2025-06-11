from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsAssetPoolsToAssetPoolModel(BaseModel):
    asset_pool_id: StrictInt | None
    asset_pool_name: StrictStr | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsAssetPoolsToAssetPoolModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsAssetPoolsToAssetPoolModel: ...
