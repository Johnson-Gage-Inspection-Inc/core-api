from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_service_records_to_asset_service_record_response_model import (
    QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel as QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    asset_service_record_id: str,
    *,
    client: AuthenticatedClient | Client,
    model_asset_service_record_id: Unset | int = ...,
) -> Response[QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel]: ...
def sync(
    asset_service_record_id: str,
    *,
    client: AuthenticatedClient | Client,
    model_asset_service_record_id: Unset | int = ...,
) -> QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel | None: ...
async def asyncio_detailed(
    asset_service_record_id: str,
    *,
    client: AuthenticatedClient | Client,
    model_asset_service_record_id: Unset | int = ...,
) -> Response[QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel]: ...
async def asyncio(
    asset_service_record_id: str,
    *,
    client: AuthenticatedClient | Client,
    model_asset_service_record_id: Unset | int = ...,
) -> QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel | None: ...
