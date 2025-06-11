from _typeshed import Incomplete
from pydantic import Field as Field, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import (
    ApiTypeError as ApiTypeError,
    ApiValueError as ApiValueError,
)
from qualer_sdk.models.qualer_api_models_asset_from_update_filter_preference_model import (
    QualerApiModelsAssetFromUpdateFilterPreferenceModel as QualerApiModelsAssetFromUpdateFilterPreferenceModel,
)
from qualer_sdk.models.qualer_api_models_asset_to_employee_filter_preference_response_model import (
    QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel as QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel,
)
from typing_extensions import Annotated

class EmployeeFilterPreferenceApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def get_employee_filter_preferences(
        self, **kwargs
    ) -> list[QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel]: ...
    @validate_arguments
    def get_employee_filter_preferences_with_http_info(
        self, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def update_employee_filter_preference(
        self,
        model: Annotated[QualerApiModelsAssetFromUpdateFilterPreferenceModel, None],
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def update_employee_filter_preference_with_http_info(
        self,
        model: Annotated[QualerApiModelsAssetFromUpdateFilterPreferenceModel, None],
        **kwargs,
    ) -> ApiResponse: ...
