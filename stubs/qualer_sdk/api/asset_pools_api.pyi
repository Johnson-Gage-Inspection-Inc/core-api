from _typeshed import Incomplete
from pydantic import StrictInt as StrictInt, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from qualer_sdk.models.qualer_api_models_asset_pools_to_asset_pool_model import QualerApiModelsAssetPoolsToAssetPoolModel as QualerApiModelsAssetPoolsToAssetPoolModel

class AssetPoolsApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def get(self, id: StrictInt, **kwargs) -> QualerApiModelsAssetPoolsToAssetPoolModel: ...
    @validate_arguments
    def get_with_http_info(self, id: StrictInt, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def get_all(self, **kwargs) -> list[QualerApiModelsAssetPoolsToAssetPoolModel]: ...
    @validate_arguments
    def get_all_with_http_info(self, **kwargs) -> ApiResponse: ...
