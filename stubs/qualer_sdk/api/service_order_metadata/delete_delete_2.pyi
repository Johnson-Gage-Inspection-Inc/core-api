from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.delete_delete_2_response_200 import (
    DeleteDelete2Response200 as DeleteDelete2Response200,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    service_order_metadata_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteDelete2Response200]: ...
def sync(
    service_order_id: int,
    service_order_metadata_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteDelete2Response200 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    service_order_metadata_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteDelete2Response200]: ...
async def asyncio(
    service_order_id: int,
    service_order_metadata_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteDelete2Response200 | None: ...
