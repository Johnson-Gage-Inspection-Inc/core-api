from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.delete_work_item_task_response_200 import (
    DeleteWorkItemTaskResponse200 as DeleteWorkItemTaskResponse200,
)
from ...types import Response as Response

def sync_detailed(
    work_item_id: int, task_id: int, *, client: AuthenticatedClient | Client
) -> Response[DeleteWorkItemTaskResponse200]: ...
def sync(
    work_item_id: int, task_id: int, *, client: AuthenticatedClient | Client
) -> DeleteWorkItemTaskResponse200 | None: ...
async def asyncio_detailed(
    work_item_id: int, task_id: int, *, client: AuthenticatedClient | Client
) -> Response[DeleteWorkItemTaskResponse200]: ...
async def asyncio(
    work_item_id: int, task_id: int, *, client: AuthenticatedClient | Client
) -> DeleteWorkItemTaskResponse200 | None: ...
