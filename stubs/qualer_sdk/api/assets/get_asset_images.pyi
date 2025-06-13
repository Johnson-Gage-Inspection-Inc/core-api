from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...types import Response as Response

def sync_detailed(
    id: int, *, client: AuthenticatedClient | Client
) -> Response[list[str]]: ...
def sync(id: int, *, client: AuthenticatedClient | Client) -> list[str] | None: ...
async def asyncio_detailed(
    id: int, *, client: AuthenticatedClient | Client
) -> Response[list[str]]: ...
async def asyncio(
    id: int, *, client: AuthenticatedClient | Client
) -> list[str] | None: ...
