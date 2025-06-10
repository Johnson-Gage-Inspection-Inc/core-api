from datetime import datetime
from pydantic import BaseModel, StrictStr as StrictStr

class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementToolResponseModel(BaseModel):
    last_service_date: datetime | None
    next_service_date: datetime | None
    calibrated_by: StrictStr | None
    certificate_number: StrictStr | None
    tool_name: StrictStr | None
    tool_description: StrictStr | None
    manufacturer: StrictStr | None
    manufacturer_part_number: StrictStr | None
    serial_number: StrictStr | None
    asset_tag: StrictStr | None
    asset_user: StrictStr | None
    equipment_id: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementToolResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModelMeasurementToolResponseModel: ...
