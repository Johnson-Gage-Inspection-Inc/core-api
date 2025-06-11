from datetime import datetime
from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
    conlist as conlist,
)
from qualer_sdk.models.qualer_api_models_clients_to_employee_employee_department_response import (
    QualerApiModelsClientsToEmployeeEmployeeDepartmentResponse as QualerApiModelsClientsToEmployeeEmployeeDepartmentResponse,
)

class QualerApiModelsClientsToEmployeeResponseModel(BaseModel):
    employee_id: StrictInt | None
    first_name: StrictStr | None
    last_name: StrictStr | None
    company_id: StrictInt | None
    login_email: StrictStr | None
    departments: None | None
    subscription_email: StrictStr | None
    subscription_phone: StrictStr | None
    office_phone: StrictStr | None
    is_locked: StrictBool | None
    image_url: StrictStr | None
    alias: StrictStr | None
    title: StrictStr | None
    is_deleted: StrictBool | None
    last_seen_date_utc: datetime | None
    culture_name: StrictStr | None
    culture_ui_name: StrictStr | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsClientsToEmployeeResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsClientsToEmployeeResponseModel: ...
