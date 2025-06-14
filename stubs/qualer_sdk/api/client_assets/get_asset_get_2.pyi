from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_to_asset_response_model import (
    QualerApiModelsAssetToAssetResponseModel as QualerApiModelsAssetToAssetResponseModel,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    asset_id_path: str,
    *,
    client: AuthenticatedClient | Client,
    asset_id_query: Unset | str = ...,
    model_asset_id: Unset | int = ...,
) -> Response[QualerApiModelsAssetToAssetResponseModel]: ...
def sync(
    asset_id_path: str,
    *,
    client: AuthenticatedClient | Client,
    asset_id_query: Unset | str = ...,
    model_asset_id: Unset | int = ...,
) -> QualerApiModelsAssetToAssetResponseModel | None: ...
async def asyncio_detailed(
    asset_id_path: str,
    *,
    client: AuthenticatedClient | Client,
    asset_id_query: Unset | str = ...,
    model_asset_id: Unset | int = ...,
) -> Response[QualerApiModelsAssetToAssetResponseModel]: ...
async def asyncio(
    asset_id_path: str,
    *,
    client: AuthenticatedClient | Client,
    asset_id_query: Unset | str = ...,
    model_asset_id: Unset | int = ...,
) -> QualerApiModelsAssetToAssetResponseModel | None: ...
