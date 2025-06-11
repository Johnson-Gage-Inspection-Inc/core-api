from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr
from qualer_sdk.models.qualer_core_shared_models_service_order_metadata_service_order_metadata_exhibits import (
    QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits as QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits,
)

class QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel(BaseModel):
    service_order_metadata_id: StrictInt | None
    metadata: StrictStr | None
    exhibits: (
        QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits | None
    )

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel: ...
