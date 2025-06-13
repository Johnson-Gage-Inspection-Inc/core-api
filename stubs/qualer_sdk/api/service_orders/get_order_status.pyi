from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.get_order_status_response_200 import (
    GetOrderStatusResponse200 as GetOrderStatusResponse200,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[Any | GetOrderStatusResponse200]: ...
def sync(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Any | GetOrderStatusResponse200 | None: ...
async def asyncio_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[Any | GetOrderStatusResponse200]: ...
async def asyncio(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Any | GetOrderStatusResponse200 | None: ...
