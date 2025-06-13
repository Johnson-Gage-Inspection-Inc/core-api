from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_service_records_to_asset_service_record_response_model import (
    QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel as QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    asset_id: int, *, client: AuthenticatedClient | Client
) -> Response[
    list["QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel"]
]: ...
def sync(
    asset_id: int, *, client: AuthenticatedClient | Client
) -> (
    list["QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel"] | None
): ...
async def asyncio_detailed(
    asset_id: int, *, client: AuthenticatedClient | Client
) -> Response[
    list["QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel"]
]: ...
async def asyncio(
    asset_id: int, *, client: AuthenticatedClient | Client
) -> (
    list["QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel"] | None
): ...
