from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
    conlist as conlist,
)
from qualer_sdk.models.qualer_api_models_maintenance_plans_to_maintenance_task_response import (
    QualerApiModelsMaintenancePlansToMaintenanceTaskResponse as QualerApiModelsMaintenancePlansToMaintenanceTaskResponse,
)

class QualerApiModelsMaintenancePlansToMaintenancePlanResponse(BaseModel):
    maintenance_plan_id: StrictInt | None
    maintenance_plan_name: StrictStr | None
    is_template: StrictBool | None
    company_name: StrictStr | None
    maintenance_tasks: None | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsMaintenancePlansToMaintenancePlanResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsMaintenancePlansToMaintenancePlanResponse: ...
