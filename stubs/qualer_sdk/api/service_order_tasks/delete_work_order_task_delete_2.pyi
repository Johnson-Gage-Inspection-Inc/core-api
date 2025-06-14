from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.delete_work_order_task_delete_2_response_204 import (
    DeleteWorkOrderTaskDelete2Response204 as DeleteWorkOrderTaskDelete2Response204,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    service_order_task_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteWorkOrderTaskDelete2Response204]: ...
def sync(
    service_order_id: int,
    service_order_task_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteWorkOrderTaskDelete2Response204 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    service_order_task_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteWorkOrderTaskDelete2Response204]: ...
async def asyncio(
    service_order_id: int,
    service_order_task_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteWorkOrderTaskDelete2Response204 | None: ...
