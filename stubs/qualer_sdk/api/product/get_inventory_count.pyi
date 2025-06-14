from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_inventory_to_inventory_response_model import (
    QualerApiModelsInventoryToInventoryResponseModel as QualerApiModelsInventoryToInventoryResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsInventoryToInventoryResponseModel"]]: ...
def sync(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsInventoryToInventoryResponseModel"] | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsInventoryToInventoryResponseModel"]]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsInventoryToInventoryResponseModel"] | None: ...
