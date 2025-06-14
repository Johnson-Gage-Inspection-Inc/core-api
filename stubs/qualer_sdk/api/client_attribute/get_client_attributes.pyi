from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.get_client_attributes_response_200 import (
    GetClientAttributesResponse200 as GetClientAttributesResponse200,
)
from ...types import Response as Response

def sync_detailed(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> Response[GetClientAttributesResponse200]: ...
def sync(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> GetClientAttributesResponse200 | None: ...
async def asyncio_detailed(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> Response[GetClientAttributesResponse200]: ...
async def asyncio(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> GetClientAttributesResponse200 | None: ...
