from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.download_document_response_200 import (
    DownloadDocumentResponse200 as DownloadDocumentResponse200,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    asset_service_record_id_path: str,
    file_name_path: str,
    *,
    client: AuthenticatedClient | Client,
    asset_service_record_id_query: Unset | str = ...,
    file_name_query: Unset | str = ...,
    model_asset_service_record_id: Unset | int = ...,
    model_file_name: Unset | str = ...,
) -> Response[DownloadDocumentResponse200]: ...
def sync(
    asset_service_record_id_path: str,
    file_name_path: str,
    *,
    client: AuthenticatedClient | Client,
    asset_service_record_id_query: Unset | str = ...,
    file_name_query: Unset | str = ...,
    model_asset_service_record_id: Unset | int = ...,
    model_file_name: Unset | str = ...,
) -> DownloadDocumentResponse200 | None: ...
async def asyncio_detailed(
    asset_service_record_id_path: str,
    file_name_path: str,
    *,
    client: AuthenticatedClient | Client,
    asset_service_record_id_query: Unset | str = ...,
    file_name_query: Unset | str = ...,
    model_asset_service_record_id: Unset | int = ...,
    model_file_name: Unset | str = ...,
) -> Response[DownloadDocumentResponse200]: ...
async def asyncio(
    asset_service_record_id_path: str,
    file_name_path: str,
    *,
    client: AuthenticatedClient | Client,
    asset_service_record_id_query: Unset | str = ...,
    file_name_query: Unset | str = ...,
    model_asset_service_record_id: Unset | int = ...,
    model_file_name: Unset | str = ...,
) -> DownloadDocumentResponse200 | None: ...
