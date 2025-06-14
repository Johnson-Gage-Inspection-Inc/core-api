from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_to_asset_response_model import (
    QualerApiModelsAssetToAssetResponseModel as QualerApiModelsAssetToAssetResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsAssetToAssetResponseModel]: ...
def sync(
    id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsAssetToAssetResponseModel | None: ...
async def asyncio_detailed(
    id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsAssetToAssetResponseModel]: ...
async def asyncio(
    id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsAssetToAssetResponseModel | None: ...
