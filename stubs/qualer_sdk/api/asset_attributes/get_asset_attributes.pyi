from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_attributes_to_asset_attributes_response import (
    QualerApiModelsAssetAttributesToAssetAttributesResponse as QualerApiModelsAssetAttributesToAssetAttributesResponse,
)
from ...types import Response as Response

def sync_detailed(
    asset_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsAssetAttributesToAssetAttributesResponse"]]: ...
def sync(
    asset_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsAssetAttributesToAssetAttributesResponse"] | None: ...
async def asyncio_detailed(
    asset_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsAssetAttributesToAssetAttributesResponse"]]: ...
async def asyncio(
    asset_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsAssetAttributesToAssetAttributesResponse"] | None: ...
