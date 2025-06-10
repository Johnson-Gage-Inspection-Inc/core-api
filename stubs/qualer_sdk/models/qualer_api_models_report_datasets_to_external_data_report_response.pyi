from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsReportDatasetsToExternalDataReportResponse(BaseModel):
    measurement_set_id: StrictInt | None
    service_order_item_id: StrictInt | None
    row: StrictInt | None
    a: StrictStr | None
    b: StrictStr | None
    c: StrictStr | None
    d: StrictStr | None
    e: StrictStr | None
    f: StrictStr | None
    g: StrictStr | None
    h: StrictStr | None
    i: StrictStr | None
    j: StrictStr | None
    k: StrictStr | None
    l: StrictStr | None
    m: StrictStr | None
    n: StrictStr | None
    o: StrictStr | None
    p: StrictStr | None
    q: StrictStr | None
    r: StrictStr | None
    s: StrictStr | None
    t: StrictStr | None
    u: StrictStr | None
    v: StrictStr | None
    w: StrictStr | None
    x: StrictStr | None
    y: StrictStr | None
    z: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsReportDatasetsToExternalDataReportResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsReportDatasetsToExternalDataReportResponse: ...
