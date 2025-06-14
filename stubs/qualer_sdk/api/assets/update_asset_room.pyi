from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_from_update_asset_room_model import (
    QualerApiModelsAssetFromUpdateAssetRoomModel as QualerApiModelsAssetFromUpdateAssetRoomModel,
)
from ...models.update_asset_room_response_200 import (
    UpdateAssetRoomResponse200 as UpdateAssetRoomResponse200,
)
from ...types import Response as Response

def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateAssetRoomModel,
) -> Response[UpdateAssetRoomResponse200]: ...
def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateAssetRoomModel,
) -> UpdateAssetRoomResponse200 | None: ...
async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateAssetRoomModel,
) -> Response[UpdateAssetRoomResponse200]: ...
async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateAssetRoomModel,
) -> UpdateAssetRoomResponse200 | None: ...
