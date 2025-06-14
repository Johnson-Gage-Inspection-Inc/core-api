from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.delete_work_order_task_response_204 import (
    DeleteWorkOrderTaskResponse204 as DeleteWorkOrderTaskResponse204,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    service_order_item_part_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteWorkOrderTaskResponse204]: ...
def sync(
    service_order_id: int,
    service_order_item_part_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteWorkOrderTaskResponse204 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    service_order_item_part_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteWorkOrderTaskResponse204]: ...
async def asyncio(
    service_order_id: int,
    service_order_item_part_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteWorkOrderTaskResponse204 | None: ...
