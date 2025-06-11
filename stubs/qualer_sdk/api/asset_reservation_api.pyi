from _typeshed import Incomplete
from datetime import datetime
from pydantic import StrictInt as StrictInt, StrictStr as StrictStr, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import (
    ApiTypeError as ApiTypeError,
    ApiValueError as ApiValueError,
)
from qualer_sdk.models.qualer_api_models_asset_reservation_from_upsert_asset_reservation_model import (
    QualerApiModelsAssetReservationFromUpsertAssetReservationModel as QualerApiModelsAssetReservationFromUpsertAssetReservationModel,
)
from qualer_sdk.models.qualer_api_models_asset_reservation_to_asset_reservation_response import (
    QualerApiModelsAssetReservationToAssetReservationResponse as QualerApiModelsAssetReservationToAssetReservationResponse,
)
from qualer_sdk.models.qualer_api_models_asset_reservation_to_upsert_asset_reservation_response import (
    QualerApiModelsAssetReservationToUpsertAssetReservationResponse as QualerApiModelsAssetReservationToUpsertAssetReservationResponse,
)

class AssetReservationApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def close(
        self,
        model_asset_id: StrictInt | None = None,
        model_area_id: StrictInt | None = None,
        model_product_id: StrictInt | None = None,
        model_serial_number: StrictStr | None = None,
        model_asset_tag: StrictStr | None = None,
        model_reservation_id: StrictInt | None = None,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def close_with_http_info(
        self,
        model_asset_id: StrictInt | None = None,
        model_area_id: StrictInt | None = None,
        model_product_id: StrictInt | None = None,
        model_serial_number: StrictStr | None = None,
        model_asset_tag: StrictStr | None = None,
        model_reservation_id: StrictInt | None = None,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def get_get2(
        self,
        model_from: datetime | None = None,
        model_to: datetime | None = None,
        model_asset_id: StrictInt | None = None,
        model_area_id: StrictInt | None = None,
        model_product_id: StrictInt | None = None,
        model_serial_number: StrictStr | None = None,
        model_asset_tag: StrictStr | None = None,
        model_reservation_id: StrictInt | None = None,
        **kwargs,
    ) -> list[QualerApiModelsAssetReservationToAssetReservationResponse]: ...
    @validate_arguments
    def get_get2_with_http_info(
        self,
        model_from: datetime | None = None,
        model_to: datetime | None = None,
        model_asset_id: StrictInt | None = None,
        model_area_id: StrictInt | None = None,
        model_product_id: StrictInt | None = None,
        model_serial_number: StrictStr | None = None,
        model_asset_tag: StrictStr | None = None,
        model_reservation_id: StrictInt | None = None,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def upsert(
        self,
        model: QualerApiModelsAssetReservationFromUpsertAssetReservationModel,
        **kwargs,
    ) -> QualerApiModelsAssetReservationToUpsertAssetReservationResponse: ...
    @validate_arguments
    def upsert_with_http_info(
        self,
        model: QualerApiModelsAssetReservationFromUpsertAssetReservationModel,
        **kwargs,
    ) -> ApiResponse: ...
