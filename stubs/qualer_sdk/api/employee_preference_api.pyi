from _typeshed import Incomplete
from pydantic import StrictStr as StrictStr, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from qualer_sdk.models.qualer_api_models_asset_to_employee_preference_response_model import QualerApiModelsAssetToEmployeePreferenceResponseModel as QualerApiModelsAssetToEmployeePreferenceResponseModel

class EmployeePreferenceApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def delete(self, element_page: StrictStr, **kwargs) -> object: ...
    @validate_arguments
    def delete_with_http_info(self, element_page: StrictStr, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def get_get4(self, element_page: StrictStr, **kwargs) -> list[QualerApiModelsAssetToEmployeePreferenceResponseModel]: ...
    @validate_arguments
    def get_get4_with_http_info(self, element_page: StrictStr, **kwargs) -> ApiResponse: ...
