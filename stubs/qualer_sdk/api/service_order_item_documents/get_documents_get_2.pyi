from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.get_documents_get_2_response_200 import (
    GetDocumentsGet2Response200 as GetDocumentsGet2Response200,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    service_order_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_file_name: Unset | str = ...,
) -> Response[Any | GetDocumentsGet2Response200]: ...
def sync(
    service_order_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_file_name: Unset | str = ...,
) -> Any | GetDocumentsGet2Response200 | None: ...
async def asyncio_detailed(
    service_order_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_file_name: Unset | str = ...,
) -> Response[Any | GetDocumentsGet2Response200]: ...
async def asyncio(
    service_order_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_file_name: Unset | str = ...,
) -> Any | GetDocumentsGet2Response200 | None: ...
