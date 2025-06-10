from datetime import datetime
from pydantic import BaseModel, StrictBool as StrictBool, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsReportDatasetsToReferenceStandardResponse(BaseModel):
    is_auxiliary: StrictBool | None
    last_service_date: datetime | None
    next_service_date: datetime | None
    certificate_number: StrictStr | None
    calibrated_by: StrictStr | None
    tool_name: StrictStr | None
    tool_site: StrictStr | None
    tool_room: StrictStr | None
    tool_station: StrictStr | None
    tool_location: StrictStr | None
    asset_tag: StrictStr | None
    lot_number: StrictStr | None
    asset_user: StrictStr | None
    tool_type_name: StrictStr | None
    tool_description: StrictStr | None
    tool_id: StrictInt | None
    manufacturer: StrictStr | None
    serial_number: StrictStr | None
    area: StrictStr | None
    service_order_item_id: StrictInt | None
    manufacturer_part_number: StrictStr | None
    equipment_id: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsReportDatasetsToReferenceStandardResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsReportDatasetsToReferenceStandardResponse: ...
