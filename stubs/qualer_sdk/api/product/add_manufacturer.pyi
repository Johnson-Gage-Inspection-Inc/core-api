from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.add_manufacturer_response_200 import (
    AddManufacturerResponse200 as AddManufacturerResponse200,
)
from ...types import UNSET as UNSET
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client, manufacturer_name: str
) -> Response[AddManufacturerResponse200]: ...
def sync(
    *, client: AuthenticatedClient | Client, manufacturer_name: str
) -> AddManufacturerResponse200 | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client, manufacturer_name: str
) -> Response[AddManufacturerResponse200]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client, manufacturer_name: str
) -> AddManufacturerResponse200 | None: ...
