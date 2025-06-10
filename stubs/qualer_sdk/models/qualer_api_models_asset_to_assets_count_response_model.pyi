from pydantic import BaseModel, StrictInt as StrictInt

class QualerApiModelsAssetToAssetsCountResponseModel(BaseModel):
    assets_all: StrictInt | None
    assets_collected: StrictInt | None
    assets_recently_serviced: StrictInt | None
    assets_due: StrictInt | None
    assets_past_due: StrictInt | None
    assets_service_pending: StrictInt | None
    assets_recently_purchased: StrictInt | None
    assets_warranty_expires: StrictInt | None
    assets_due_for_replacement: StrictInt | None
    assets_out_of_service: StrictInt | None
    assets_not_serviced: StrictInt | None
    assets_without_schedule: StrictInt | None
    assets_without_vendor: StrictInt | None
    assets_without_product: StrictInt | None
    assets_added: StrictInt | None
    assets_updated: StrictInt | None
    assets_deleted: StrictInt | None
    assets_no_agreement: StrictInt | None
    assets_expired_agreement: StrictInt | None
    assets_expiring_soon_agreement: StrictInt | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsAssetToAssetsCountResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsAssetToAssetsCountResponseModel: ...
