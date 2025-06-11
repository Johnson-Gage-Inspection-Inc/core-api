from _typeshed import Incomplete
from datetime import datetime
from pydantic import StrictInt as StrictInt, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import (
    ApiTypeError as ApiTypeError,
    ApiValueError as ApiValueError,
)
from qualer_sdk.models.qualer_api_models_measurements_to_measurement_record_response_model import (
    QualerApiModelsMeasurementsToMeasurementRecordResponseModel as QualerApiModelsMeasurementsToMeasurementRecordResponseModel,
)

class AssetMeasurementsApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def get_measurements_by_asset(
        self,
        asset_id: StrictInt,
        var_from: datetime | None = None,
        to: datetime | None = None,
        **kwargs,
    ) -> list[QualerApiModelsMeasurementsToMeasurementRecordResponseModel]: ...
    @validate_arguments
    def get_measurements_by_asset_with_http_info(
        self,
        asset_id: StrictInt,
        var_from: datetime | None = None,
        to: datetime | None = None,
        **kwargs,
    ) -> ApiResponse: ...
