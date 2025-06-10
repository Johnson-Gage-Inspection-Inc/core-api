from pydantic import BaseModel, StrictStr as StrictStr, conlist as conlist
from qualer_sdk.models.qualer_core_shared_models_service_order_metadata_service_order_metadata_exhibits_key_value import QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibitsKeyValue as QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibitsKeyValue

class QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits(BaseModel):
    title: StrictStr | None
    subtitle: StrictStr | None
    exhibits: None | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits: ...
