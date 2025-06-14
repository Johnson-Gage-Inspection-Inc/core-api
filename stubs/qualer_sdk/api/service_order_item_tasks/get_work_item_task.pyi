from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.get_work_item_task_response_200 import (
    GetWorkItemTaskResponse200 as GetWorkItemTaskResponse200,
)
from ...types import Response as Response

def sync_detailed(
    work_item_id: int, task_id: int, *, client: AuthenticatedClient | Client
) -> Response[GetWorkItemTaskResponse200]: ...
def sync(
    work_item_id: int, task_id: int, *, client: AuthenticatedClient | Client
) -> GetWorkItemTaskResponse200 | None: ...
async def asyncio_detailed(
    work_item_id: int, task_id: int, *, client: AuthenticatedClient | Client
) -> Response[GetWorkItemTaskResponse200]: ...
async def asyncio(
    work_item_id: int, task_id: int, *, client: AuthenticatedClient | Client
) -> GetWorkItemTaskResponse200 | None: ...
