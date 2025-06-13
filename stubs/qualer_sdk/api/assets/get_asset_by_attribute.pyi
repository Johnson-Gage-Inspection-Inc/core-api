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
    *,
    client: AuthenticatedClient | Client,
    model_name: Unset | str = ...,
    model_value: Unset | str = ...,
) -> Response[list["QualerApiModelsAssetToAssetResponseModel"]]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    model_name: Unset | str = ...,
    model_value: Unset | str = ...,
) -> list["QualerApiModelsAssetToAssetResponseModel"] | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    model_name: Unset | str = ...,
    model_value: Unset | str = ...,
) -> Response[list["QualerApiModelsAssetToAssetResponseModel"]]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    model_name: Unset | str = ...,
    model_value: Unset | str = ...,
) -> list["QualerApiModelsAssetToAssetResponseModel"] | None: ...
