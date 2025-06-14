import datetime

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
    *,
    client: AuthenticatedClient | Client,
    model_asset_id: Unset | int = ...,
    model_serial_number: Unset | str = ...,
    model_from: Unset | datetime.datetime = ...,
    model_to: Unset | datetime.datetime = ...,
) -> Response[QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    model_asset_id: Unset | int = ...,
    model_serial_number: Unset | str = ...,
    model_from: Unset | datetime.datetime = ...,
    model_to: Unset | datetime.datetime = ...,
) -> QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    model_asset_id: Unset | int = ...,
    model_serial_number: Unset | str = ...,
    model_from: Unset | datetime.datetime = ...,
    model_to: Unset | datetime.datetime = ...,
) -> Response[QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    model_asset_id: Unset | int = ...,
    model_serial_number: Unset | str = ...,
    model_from: Unset | datetime.datetime = ...,
    model_to: Unset | datetime.datetime = ...,
) -> QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel | None: ...
