from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.get_work_item_charges_response_200 import (
    GetWorkItemChargesResponse200 as GetWorkItemChargesResponse200,
)
from ...types import Response as Response

def sync_detailed(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[GetWorkItemChargesResponse200]: ...
def sync(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> GetWorkItemChargesResponse200 | None: ...
async def asyncio_detailed(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[GetWorkItemChargesResponse200]: ...
async def asyncio(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> GetWorkItemChargesResponse200 | None: ...
