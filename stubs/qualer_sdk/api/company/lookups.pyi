from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.lookups_lookup_type import LookupsLookupType as LookupsLookupType
from ...types import UNSET as UNSET
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client, lookup_type: LookupsLookupType
) -> Response[list[str]]: ...
def sync(
    *, client: AuthenticatedClient | Client, lookup_type: LookupsLookupType
) -> list[str] | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client, lookup_type: LookupsLookupType
) -> Response[list[str]]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client, lookup_type: LookupsLookupType
) -> list[str] | None: ...
