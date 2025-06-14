from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_service_records_from_update_asset_service_record_model import (
    QualerApiModelsAssetServiceRecordsFromUpdateAssetServiceRecordModel as QualerApiModelsAssetServiceRecordsFromUpdateAssetServiceRecordModel,
)
from ...models.update_asset_service_record_response_200 import (
    UpdateAssetServiceRecordResponse200 as UpdateAssetServiceRecordResponse200,
)
from ...types import Response as Response

def sync_detailed(
    asset_service_record_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetServiceRecordsFromUpdateAssetServiceRecordModel,
) -> Response[UpdateAssetServiceRecordResponse200]: ...
def sync(
    asset_service_record_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetServiceRecordsFromUpdateAssetServiceRecordModel,
) -> UpdateAssetServiceRecordResponse200 | None: ...
async def asyncio_detailed(
    asset_service_record_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetServiceRecordsFromUpdateAssetServiceRecordModel,
) -> Response[UpdateAssetServiceRecordResponse200]: ...
async def asyncio(
    asset_service_record_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetServiceRecordsFromUpdateAssetServiceRecordModel,
) -> UpdateAssetServiceRecordResponse200 | None: ...
