from _typeshed import Incomplete
from pydantic import StrictInt as StrictInt, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from qualer_sdk.models.qualer_api_models_asset_to_asset_service_forecast_model import QualerApiModelsAssetToAssetServiceForecastModel as QualerApiModelsAssetToAssetServiceForecastModel

class AssetServiceForecastApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def get_asset_forecast_list(self, **kwargs) -> list[QualerApiModelsAssetToAssetServiceForecastModel]: ...
    @validate_arguments
    def get_asset_forecast_list_with_http_info(self, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def get_client_asset_forecast_list(self, client_company_id: StrictInt, **kwargs) -> list[QualerApiModelsAssetToAssetServiceForecastModel]: ...
    @validate_arguments
    def get_client_asset_forecast_list_with_http_info(self, client_company_id: StrictInt, **kwargs) -> ApiResponse: ...
