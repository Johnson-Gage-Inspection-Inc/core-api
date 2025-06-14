from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_pools_to_asset_pool_model import (
    QualerApiModelsAssetPoolsToAssetPoolModel as QualerApiModelsAssetPoolsToAssetPoolModel,
)
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsAssetPoolsToAssetPoolModel"]]: ...
def sync(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsAssetPoolsToAssetPoolModel"] | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsAssetPoolsToAssetPoolModel"]]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsAssetPoolsToAssetPoolModel"] | None: ...
