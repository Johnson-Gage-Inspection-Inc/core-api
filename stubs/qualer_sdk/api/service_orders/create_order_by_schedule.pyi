from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.create_order_by_schedule_response_200 import (
    CreateOrderByScheduleResponse200 as CreateOrderByScheduleResponse200,
)
from ...types import Response as Response

def sync_detailed(
    service_schedule_id: int, *, client: AuthenticatedClient | Client
) -> Response[CreateOrderByScheduleResponse200]: ...
def sync(
    service_schedule_id: int, *, client: AuthenticatedClient | Client
) -> CreateOrderByScheduleResponse200 | None: ...
async def asyncio_detailed(
    service_schedule_id: int, *, client: AuthenticatedClient | Client
) -> Response[CreateOrderByScheduleResponse200]: ...
async def asyncio(
    service_schedule_id: int, *, client: AuthenticatedClient | Client
) -> CreateOrderByScheduleResponse200 | None: ...
