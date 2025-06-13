from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.upload_documents_post_3_response_200 import (
    UploadDocumentsPost3Response200 as UploadDocumentsPost3Response200,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    service_order_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_report_type: Unset | str = ...,
    model_is_private: Unset | bool = ...,
) -> Response[UploadDocumentsPost3Response200]: ...
def sync(
    service_order_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_report_type: Unset | str = ...,
    model_is_private: Unset | bool = ...,
) -> UploadDocumentsPost3Response200 | None: ...
async def asyncio_detailed(
    service_order_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_report_type: Unset | str = ...,
    model_is_private: Unset | bool = ...,
) -> Response[UploadDocumentsPost3Response200]: ...
async def asyncio(
    service_order_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_report_type: Unset | str = ...,
    model_is_private: Unset | bool = ...,
) -> UploadDocumentsPost3Response200 | None: ...
