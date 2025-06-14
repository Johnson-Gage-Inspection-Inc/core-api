from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.get_work_item_image_response_200 import (
    GetWorkItemImageResponse200 as GetWorkItemImageResponse200,
)
from ...types import Response as Response

def sync_detailed(
    work_item_id: int, image_name: str, *, client: AuthenticatedClient | Client
) -> Response[GetWorkItemImageResponse200]: ...
def sync(
    work_item_id: int, image_name: str, *, client: AuthenticatedClient | Client
) -> GetWorkItemImageResponse200 | None: ...
async def asyncio_detailed(
    work_item_id: int, image_name: str, *, client: AuthenticatedClient | Client
) -> Response[GetWorkItemImageResponse200]: ...
async def asyncio(
    work_item_id: int, image_name: str, *, client: AuthenticatedClient | Client
) -> GetWorkItemImageResponse200 | None: ...
