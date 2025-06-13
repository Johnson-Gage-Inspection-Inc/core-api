from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.collect_assets_response_200 import (
    CollectAssetsResponse200 as CollectAssetsResponse200,
)
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client, body: list[int]
) -> Response[CollectAssetsResponse200]: ...
def sync(
    *, client: AuthenticatedClient | Client, body: list[int]
) -> CollectAssetsResponse200 | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client, body: list[int]
) -> Response[CollectAssetsResponse200]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client, body: list[int]
) -> CollectAssetsResponse200 | None: ...
