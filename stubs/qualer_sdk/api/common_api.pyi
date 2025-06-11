from _typeshed import Incomplete
from pydantic import StrictStr as StrictStr, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import (
    ApiTypeError as ApiTypeError,
    ApiValueError as ApiValueError,
)
from qualer_sdk.models.qualer_api_models_common_to_culture_list_response_model import (
    QualerApiModelsCommonToCultureListResponseModel as QualerApiModelsCommonToCultureListResponseModel,
)
from qualer_sdk.models.qualer_api_models_common_to_setting_response_model import (
    QualerApiModelsCommonToSettingResponseModel as QualerApiModelsCommonToSettingResponseModel,
)

class CommonApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def culture_list(
        self, **kwargs
    ) -> QualerApiModelsCommonToCultureListResponseModel: ...
    @validate_arguments
    def culture_list_with_http_info(self, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def culture_ui_list(
        self, **kwargs
    ) -> QualerApiModelsCommonToCultureListResponseModel: ...
    @validate_arguments
    def culture_ui_list_with_http_info(self, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def get_company_settings(
        self, setting_key: StrictStr, **kwargs
    ) -> QualerApiModelsCommonToSettingResponseModel: ...
    @validate_arguments
    def get_company_settings_with_http_info(
        self, setting_key: StrictStr, **kwargs
    ) -> ApiResponse: ...
