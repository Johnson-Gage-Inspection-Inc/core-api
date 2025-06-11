from _typeshed import Incomplete
from pydantic import StrictInt as StrictInt, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import (
    ApiTypeError as ApiTypeError,
    ApiValueError as ApiValueError,
)
from qualer_sdk.models.qualer_api_models_account_from_login_response_model import (
    QualerApiModelsAccountFromLoginResponseModel as QualerApiModelsAccountFromLoginResponseModel,
)
from qualer_sdk.models.qualer_api_models_account_to_employee_event_message_response_model import (
    QualerApiModelsAccountToEmployeeEventMessageResponseModel as QualerApiModelsAccountToEmployeeEventMessageResponseModel,
)
from qualer_sdk.models.qualer_api_models_account_to_employee_event_response_model import (
    QualerApiModelsAccountToEmployeeEventResponseModel as QualerApiModelsAccountToEmployeeEventResponseModel,
)
from qualer_sdk.models.qualer_api_models_account_to_logout_model import (
    QualerApiModelsAccountToLogoutModel as QualerApiModelsAccountToLogoutModel,
)
from qualer_sdk.models.qualer_api_models_employees_from_employee_location_model import (
    QualerApiModelsEmployeesFromEmployeeLocationModel as QualerApiModelsEmployeesFromEmployeeLocationModel,
)
from qualer_sdk.models.qualer_web_mvc_areas_api_models_account_to_login_model import (
    QualerWebMvcAreasApiModelsAccountToLoginModel as QualerWebMvcAreasApiModelsAccountToLoginModel,
)

class AccountApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def companies(
        self, model: QualerWebMvcAreasApiModelsAccountToLoginModel, **kwargs
    ) -> object: ...
    @validate_arguments
    def companies_with_http_info(
        self, model: QualerWebMvcAreasApiModelsAccountToLoginModel, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_employee_message(
        self, message_id: StrictInt, **kwargs
    ) -> QualerApiModelsAccountToEmployeeEventMessageResponseModel: ...
    @validate_arguments
    def get_employee_message_with_http_info(
        self, message_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_employee_messages(
        self,
        model_period: StrictInt | None = None,
        model_site_id: StrictInt | None = None,
        **kwargs,
    ) -> list[QualerApiModelsAccountToEmployeeEventResponseModel]: ...
    @validate_arguments
    def get_employee_messages_with_http_info(
        self,
        model_period: StrictInt | None = None,
        model_site_id: StrictInt | None = None,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def login(
        self, model: QualerWebMvcAreasApiModelsAccountToLoginModel, **kwargs
    ) -> QualerApiModelsAccountFromLoginResponseModel: ...
    @validate_arguments
    def login_with_http_info(
        self, model: QualerWebMvcAreasApiModelsAccountToLoginModel, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def logout(
        self, model: QualerApiModelsAccountToLogoutModel, **kwargs
    ) -> object: ...
    @validate_arguments
    def logout_with_http_info(
        self, model: QualerApiModelsAccountToLogoutModel, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def post_employee_location(
        self, model: QualerApiModelsEmployeesFromEmployeeLocationModel, **kwargs
    ) -> object: ...
    @validate_arguments
    def post_employee_location_with_http_info(
        self, model: QualerApiModelsEmployeesFromEmployeeLocationModel, **kwargs
    ) -> ApiResponse: ...
