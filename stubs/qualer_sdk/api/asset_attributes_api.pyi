from _typeshed import Incomplete
from pydantic import StrictInt as StrictInt, conlist as conlist, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import (
    ApiTypeError as ApiTypeError,
    ApiValueError as ApiValueError,
)
from qualer_sdk.models.qualer_api_models_asset_attributes_to_asset_attributes_response import (
    QualerApiModelsAssetAttributesToAssetAttributesResponse as QualerApiModelsAssetAttributesToAssetAttributesResponse,
)
from qualer_sdk.models.qualer_api_models_common_from_attribute_model import (
    QualerApiModelsCommonFromAttributeModel as QualerApiModelsCommonFromAttributeModel,
)

class AssetAttributesApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def get_asset_attributes(
        self, asset_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsAssetAttributesToAssetAttributesResponse]: ...
    @validate_arguments
    def get_asset_attributes_with_http_info(
        self, asset_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def upsert_asset_attributes(
        self, asset_id: StrictInt, model: None, **kwargs
    ) -> object: ...
    @validate_arguments
    def upsert_asset_attributes_with_http_info(
        self, asset_id: StrictInt, model: None, **kwargs
    ) -> ApiResponse: ...
