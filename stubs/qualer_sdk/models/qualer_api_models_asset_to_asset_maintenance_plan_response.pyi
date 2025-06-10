from datetime import datetime
from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr, conlist as conlist
from qualer_sdk.models.qualer_api_models_asset_to_asset_maintenance_plan_response_assigned_employee import QualerApiModelsAssetToAssetMaintenancePlanResponseAssignedEmployee as QualerApiModelsAssetToAssetMaintenancePlanResponseAssignedEmployee

class QualerApiModelsAssetToAssetMaintenancePlanResponse(BaseModel):
    maintenance_plan_id: StrictInt | None
    maintenance_plan_name: StrictStr | None
    task_notes: StrictStr | None
    last_service_task: StrictStr | None
    last_service_date: datetime | None
    next_service_task: StrictStr | None
    next_service_date: datetime | None
    certificate_due_date: datetime | None
    owner_first_name: StrictStr | None
    owner_last_name: StrictStr | None
    owner_alias: StrictStr | None
    owner_department_name: StrictStr | None
    technician_first_name: StrictStr | None
    technician_last_name: StrictStr | None
    technician_alias: StrictStr | None
    technician_department_name: StrictStr | None
    assigned_employees: None | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsAssetToAssetMaintenancePlanResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsAssetToAssetMaintenancePlanResponse: ...
