from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_from_update_room_model import (
    QualerApiModelsAssetFromUpdateRoomModel as QualerApiModelsAssetFromUpdateRoomModel,
)
from ...models.update_room_response_200 import (
    UpdateRoomResponse200 as UpdateRoomResponse200,
)
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateRoomModel,
) -> Response[UpdateRoomResponse200]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateRoomModel,
) -> UpdateRoomResponse200 | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateRoomModel,
) -> Response[UpdateRoomResponse200]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateRoomModel,
) -> UpdateRoomResponse200 | None: ...
