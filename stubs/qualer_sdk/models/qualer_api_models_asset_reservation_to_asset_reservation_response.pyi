from datetime import datetime
from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsAssetReservationToAssetReservationResponse(BaseModel):
    original_begin_date: datetime | None
    original_end_date: datetime | None
    begin_date: datetime | None
    end_date: datetime | None
    reserved_on: datetime | None
    reserved_on_utc: datetime | None
    comments: StrictStr | None
    product_id: StrictInt | None
    asset_id: StrictInt | None
    service_order_id: StrictInt | None
    reserved_by_id: StrictInt | None
    reserved_by_name: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsAssetReservationToAssetReservationResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsAssetReservationToAssetReservationResponse: ...
