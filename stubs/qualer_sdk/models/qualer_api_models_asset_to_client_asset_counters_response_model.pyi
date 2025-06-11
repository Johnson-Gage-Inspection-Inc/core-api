from pydantic import BaseModel, StrictInt as StrictInt

class QualerApiModelsAssetToClientAssetCountersResponseModel(BaseModel):
    client_assets_collected: StrictInt | None
    client_unset: StrictInt | None
    client_due_for_service: StrictInt | None
    client_past_due: StrictInt | None
    client_out_of_service: StrictInt | None
    client_without_schedule: StrictInt | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsAssetToClientAssetCountersResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsAssetToClientAssetCountersResponseModel: ...
