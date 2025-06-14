from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_to_asset_response_model import (
    QualerApiModelsAssetToAssetResponseModel as QualerApiModelsAssetToAssetResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    barcode: str, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsAssetToAssetResponseModel"]]: ...
def sync(
    barcode: str, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsAssetToAssetResponseModel"] | None: ...
async def asyncio_detailed(
    barcode: str, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsAssetToAssetResponseModel"]]: ...
async def asyncio(
    barcode: str, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsAssetToAssetResponseModel"] | None: ...
