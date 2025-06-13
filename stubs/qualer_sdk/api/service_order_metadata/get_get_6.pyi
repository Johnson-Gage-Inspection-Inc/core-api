from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.get_get_6_response_200 import GetGet6Response200 as GetGet6Response200
from ...types import Response as Response

def sync_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[GetGet6Response200]: ...
def sync(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> GetGet6Response200 | None: ...
async def asyncio_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[GetGet6Response200]: ...
async def asyncio(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> GetGet6Response200 | None: ...
