from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsAssetReservationFromCloseAssetReservationsModel(BaseModel):
    asset_id: StrictInt | None
    area_id: StrictInt | None
    product_id: StrictInt | None
    serial_number: StrictStr | None
    asset_tag: StrictStr | None
    reservation_id: StrictInt | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsAssetReservationFromCloseAssetReservationsModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsAssetReservationFromCloseAssetReservationsModel: ...
