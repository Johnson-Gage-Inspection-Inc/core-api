from pydantic import BaseModel, StrictStr as StrictStr

class QualerApiModelsAssetFromUpdateRoomModel(BaseModel):
    room: StrictStr | None
    tracking_id: StrictStr | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsAssetFromUpdateRoomModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsAssetFromUpdateRoomModel: ...
