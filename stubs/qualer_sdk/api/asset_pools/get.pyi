from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_pools_to_asset_pool_model import (
    QualerApiModelsAssetPoolsToAssetPoolModel as QualerApiModelsAssetPoolsToAssetPoolModel,
)
from ...types import Response as Response

def sync_detailed(
    id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsAssetPoolsToAssetPoolModel]: ...
def sync(
    id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsAssetPoolsToAssetPoolModel | None: ...
async def asyncio_detailed(
    id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsAssetPoolsToAssetPoolModel]: ...
async def asyncio(
    id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsAssetPoolsToAssetPoolModel | None: ...
