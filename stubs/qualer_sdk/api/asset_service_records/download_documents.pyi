from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.download_documents_response_200 import (
    DownloadDocumentsResponse200 as DownloadDocumentsResponse200,
)
from ...types import Response as Response

def sync_detailed(
    asset_service_record_id: int, *, client: AuthenticatedClient | Client
) -> Response[DownloadDocumentsResponse200]: ...
def sync(
    asset_service_record_id: int, *, client: AuthenticatedClient | Client
) -> DownloadDocumentsResponse200 | None: ...
async def asyncio_detailed(
    asset_service_record_id: int, *, client: AuthenticatedClient | Client
) -> Response[DownloadDocumentsResponse200]: ...
async def asyncio(
    asset_service_record_id: int, *, client: AuthenticatedClient | Client
) -> DownloadDocumentsResponse200 | None: ...
