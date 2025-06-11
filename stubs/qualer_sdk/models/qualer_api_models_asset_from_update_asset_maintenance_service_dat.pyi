from datetime import datetime
from pydantic import BaseModel, StrictStr as StrictStr

class QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat(BaseModel):
    reset_service_date: datetime | None
    reset_service_task: StrictStr | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat: ...
