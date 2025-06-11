from pydantic import BaseModel, StrictBool as StrictBool

class QualerApiModelsMeasurementsFromDisplayOptions(BaseModel):
    err: StrictBool | None
    mean: StrictBool | None
    max: StrictBool | None
    min: StrictBool | None
    sd: StrictBool | None
    cv: StrictBool | None
    tar: StrictBool | None
    tur: StrictBool | None
    mu: StrictBool | None
    cmc: StrictBool | None
    tol: StrictBool | None
    delta: StrictBool | None
    range: StrictBool | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsMeasurementsFromDisplayOptions: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsMeasurementsFromDisplayOptions: ...
