from _typeshed import Incomplete
from pydantic import StrictInt as StrictInt, StrictStr as StrictStr, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import (
    ApiTypeError as ApiTypeError,
    ApiValueError as ApiValueError,
)
from qualer_sdk.models.qualer_api_models_clients_to_employee_response_model import (
    QualerApiModelsClientsToEmployeeResponseModel as QualerApiModelsClientsToEmployeeResponseModel,
)
from qualer_sdk.models.qualer_api_models_employees_from_create_employee_model import (
    QualerApiModelsEmployeesFromCreateEmployeeModel as QualerApiModelsEmployeesFromCreateEmployeeModel,
)
from qualer_sdk.models.qualer_api_models_employees_from_employee_department_model import (
    QualerApiModelsEmployeesFromEmployeeDepartmentModel as QualerApiModelsEmployeesFromEmployeeDepartmentModel,
)
from qualer_sdk.models.qualer_api_models_employees_from_update_employee_model import (
    QualerApiModelsEmployeesFromUpdateEmployeeModel as QualerApiModelsEmployeesFromUpdateEmployeeModel,
)
from qualer_sdk.models.qualer_api_models_employees_to_created_employee_response import (
    QualerApiModelsEmployeesToCreatedEmployeeResponse as QualerApiModelsEmployeesToCreatedEmployeeResponse,
)

class EmployeesApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def add_employee_department(
        self,
        employee_id: StrictInt,
        model: QualerApiModelsEmployeesFromEmployeeDepartmentModel,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def add_employee_department_with_http_info(
        self,
        employee_id: StrictInt,
        model: QualerApiModelsEmployeesFromEmployeeDepartmentModel,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def create_employee_post2(
        self, model: QualerApiModelsEmployeesFromCreateEmployeeModel, **kwargs
    ) -> QualerApiModelsEmployeesToCreatedEmployeeResponse: ...
    @validate_arguments
    def create_employee_post2_with_http_info(
        self, model: QualerApiModelsEmployeesFromCreateEmployeeModel, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def delete_employee_department(
        self, employee_id: StrictInt, department_id: StrictInt, **kwargs
    ) -> object: ...
    @validate_arguments
    def delete_employee_department_with_http_info(
        self, employee_id: StrictInt, department_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_employee_get2(
        self, employee_id: StrictInt, **kwargs
    ) -> QualerApiModelsClientsToEmployeeResponseModel: ...
    @validate_arguments
    def get_employee_get2_with_http_info(
        self, employee_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_employees_get2(
        self, model_search_string: StrictStr | None = None, **kwargs
    ) -> list[QualerApiModelsClientsToEmployeeResponseModel]: ...
    @validate_arguments
    def get_employees_get2_with_http_info(
        self, model_search_string: StrictStr | None = None, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def update_employee(
        self,
        employee_id: StrictInt,
        model: QualerApiModelsEmployeesFromUpdateEmployeeModel,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def update_employee_with_http_info(
        self,
        employee_id: StrictInt,
        model: QualerApiModelsEmployeesFromUpdateEmployeeModel,
        **kwargs,
    ) -> ApiResponse: ...
