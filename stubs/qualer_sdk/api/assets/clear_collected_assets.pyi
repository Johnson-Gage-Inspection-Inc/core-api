from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.clear_collected_assets_response_200 import (
    ClearCollectedAssetsResponse200 as ClearCollectedAssetsResponse200,
)
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client, body: list[int]
) -> Response[ClearCollectedAssetsResponse200]: ...
def sync(
    *, client: AuthenticatedClient | Client, body: list[int]
) -> ClearCollectedAssetsResponse200 | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client, body: list[int]
) -> Response[ClearCollectedAssetsResponse200]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client, body: list[int]
) -> ClearCollectedAssetsResponse200 | None: ...
