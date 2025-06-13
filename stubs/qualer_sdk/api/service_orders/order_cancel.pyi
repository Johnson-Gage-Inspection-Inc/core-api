from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.order_cancel_response_200 import (
    OrderCancelResponse200 as OrderCancelResponse200,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    reason_text: Unset | str = ...,
) -> Response[OrderCancelResponse200]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    reason_text: Unset | str = ...,
) -> OrderCancelResponse200 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    reason_text: Unset | str = ...,
) -> Response[OrderCancelResponse200]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    reason_text: Unset | str = ...,
) -> OrderCancelResponse200 | None: ...
