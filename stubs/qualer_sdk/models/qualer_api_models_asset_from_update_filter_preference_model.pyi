from datetime import datetime
from pydantic import BaseModel, StrictBool as StrictBool, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsAssetFromUpdateFilterPreferenceModel(BaseModel):
    filter_type: StrictStr | None
    within_days: StrictInt | None
    use_date_range: StrictBool | None
    start_date: datetime | None
    end_date: datetime | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsAssetFromUpdateFilterPreferenceModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsAssetFromUpdateFilterPreferenceModel: ...
