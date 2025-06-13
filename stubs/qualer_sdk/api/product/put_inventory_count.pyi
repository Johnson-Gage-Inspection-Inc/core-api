from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.put_inventory_count_response_200 import (
    PutInventoryCountResponse200 as PutInventoryCountResponse200,
)
from ...models.qualer_api_models_inventory_from_inventory_count_model import (
    QualerApiModelsInventoryFromInventoryCountModel as QualerApiModelsInventoryFromInventoryCountModel,
)
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerApiModelsInventoryFromInventoryCountModel"],
) -> Response[PutInventoryCountResponse200]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerApiModelsInventoryFromInventoryCountModel"],
) -> PutInventoryCountResponse200 | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerApiModelsInventoryFromInventoryCountModel"],
) -> Response[PutInventoryCountResponse200]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerApiModelsInventoryFromInventoryCountModel"],
) -> PutInventoryCountResponse200 | None: ...
