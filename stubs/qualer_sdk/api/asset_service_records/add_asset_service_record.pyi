from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.add_asset_service_record_response_200 import (
    AddAssetServiceRecordResponse200 as AddAssetServiceRecordResponse200,
)
from ...models.qualer_api_models_asset_service_records_from_add_asset_service_record_model import (
    QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel as QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel,
)
from ...models.qualer_api_models_asset_service_records_to_add_asset_service_record_response import (
    QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse as QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse,
)
from ...types import Response as Response

def sync_detailed(
    asset_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel,
) -> Response[
    AddAssetServiceRecordResponse200
    | QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse
]: ...
def sync(
    asset_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel,
) -> (
    AddAssetServiceRecordResponse200
    | QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse
    | None
): ...
async def asyncio_detailed(
    asset_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel,
) -> Response[
    AddAssetServiceRecordResponse200
    | QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse
]: ...
async def asyncio(
    asset_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel,
) -> (
    AddAssetServiceRecordResponse200
    | QualerApiModelsAssetServiceRecordsToAddAssetServiceRecordResponse
    | None
): ...
