from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.upload_documents_post_2_response_200 import (
    UploadDocumentsPost2Response200 as UploadDocumentsPost2Response200,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_report_type: Unset | str = ...,
    model_is_private: Unset | bool = ...,
) -> Response[UploadDocumentsPost2Response200]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_report_type: Unset | str = ...,
    model_is_private: Unset | bool = ...,
) -> UploadDocumentsPost2Response200 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_report_type: Unset | str = ...,
    model_is_private: Unset | bool = ...,
) -> Response[UploadDocumentsPost2Response200]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_report_type: Unset | str = ...,
    model_is_private: Unset | bool = ...,
) -> UploadDocumentsPost2Response200 | None: ...
