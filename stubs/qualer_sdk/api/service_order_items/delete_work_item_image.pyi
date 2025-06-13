from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.delete_work_item_image_response_200 import (
    DeleteWorkItemImageResponse200 as DeleteWorkItemImageResponse200,
)
from ...types import Response as Response

def sync_detailed(
    work_item_id: int, image_name: str, *, client: AuthenticatedClient | Client
) -> Response[DeleteWorkItemImageResponse200]: ...
def sync(
    work_item_id: int, image_name: str, *, client: AuthenticatedClient | Client
) -> DeleteWorkItemImageResponse200 | None: ...
async def asyncio_detailed(
    work_item_id: int, image_name: str, *, client: AuthenticatedClient | Client
) -> Response[DeleteWorkItemImageResponse200]: ...
async def asyncio(
    work_item_id: int, image_name: str, *, client: AuthenticatedClient | Client
) -> DeleteWorkItemImageResponse200 | None: ...
