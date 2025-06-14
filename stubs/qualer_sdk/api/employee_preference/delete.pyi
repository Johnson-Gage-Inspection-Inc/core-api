from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.delete_element_page import DeleteElementPage as DeleteElementPage
from ...models.delete_response_200 import DeleteResponse200 as DeleteResponse200
from ...types import Response as Response

def sync_detailed(
    element_page: DeleteElementPage, *, client: AuthenticatedClient | Client
) -> Response[DeleteResponse200]: ...
def sync(
    element_page: DeleteElementPage, *, client: AuthenticatedClient | Client
) -> DeleteResponse200 | None: ...
async def asyncio_detailed(
    element_page: DeleteElementPage, *, client: AuthenticatedClient | Client
) -> Response[DeleteResponse200]: ...
async def asyncio(
    element_page: DeleteElementPage, *, client: AuthenticatedClient | Client
) -> DeleteResponse200 | None: ...
