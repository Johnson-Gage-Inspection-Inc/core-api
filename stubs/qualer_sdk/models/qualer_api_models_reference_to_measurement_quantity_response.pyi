from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsReferenceToMeasurementQuantityResponse(BaseModel):
    measurement_quantity_id: StrictInt | None
    measurement_quantity: StrictStr | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsReferenceToMeasurementQuantityResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsReferenceToMeasurementQuantityResponse: ...
