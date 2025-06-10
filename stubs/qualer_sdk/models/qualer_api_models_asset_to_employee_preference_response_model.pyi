from pydantic import BaseModel, StrictBool as StrictBool, StrictStr as StrictStr, conlist as conlist

class QualerApiModelsAssetToEmployeePreferenceResponseModel(BaseModel):
    element_type: StrictStr | None
    element_page: StrictStr | None
    element_id: StrictStr | None
    preference: None | None
    is_pinned: StrictBool | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsAssetToEmployeePreferenceResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsAssetToEmployeePreferenceResponseModel: ...
