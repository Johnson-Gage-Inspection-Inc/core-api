from _typeshed import Incomplete
from pydantic import StrictInt as StrictInt, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import (
    ApiTypeError as ApiTypeError,
    ApiValueError as ApiValueError,
)
from qualer_sdk.models.qualer_api_models_asset_service_records_to_asset_service_record_response_model import (
    QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel as QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel,
)

class ClientAssetServiceRecordsApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def get_asset_service_records_by_asset_get2(
        self, asset_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel]: ...
    @validate_arguments
    def get_asset_service_records_by_asset_get2_with_http_info(
        self, asset_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
