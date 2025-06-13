from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.get_work_item_tasks_response_200 import (
    GetWorkItemTasksResponse200 as GetWorkItemTasksResponse200,
)
from ...types import Response as Response

def sync_detailed(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[GetWorkItemTasksResponse200]: ...
def sync(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> GetWorkItemTasksResponse200 | None: ...
async def asyncio_detailed(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[GetWorkItemTasksResponse200]: ...
async def asyncio(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> GetWorkItemTasksResponse200 | None: ...
