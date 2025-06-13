from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.get_documents_response_200 import (
    GetDocumentsResponse200 as GetDocumentsResponse200,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_file_name: Unset | str = ...,
) -> Response[Any | GetDocumentsResponse200]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_file_name: Unset | str = ...,
) -> Any | GetDocumentsResponse200 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_file_name: Unset | str = ...,
) -> Response[Any | GetDocumentsResponse200]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_file_name: Unset | str = ...,
) -> Any | GetDocumentsResponse200 | None: ...
