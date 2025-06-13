from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.upload_documents_response_200 import (
    UploadDocumentsResponse200 as UploadDocumentsResponse200,
)
from ...types import Response as Response

def sync_detailed(
    asset_service_record_id: int, *, client: AuthenticatedClient | Client
) -> Response[UploadDocumentsResponse200]: ...
def sync(
    asset_service_record_id: int, *, client: AuthenticatedClient | Client
) -> UploadDocumentsResponse200 | None: ...
async def asyncio_detailed(
    asset_service_record_id: int, *, client: AuthenticatedClient | Client
) -> Response[UploadDocumentsResponse200]: ...
async def asyncio(
    asset_service_record_id: int, *, client: AuthenticatedClient | Client
) -> UploadDocumentsResponse200 | None: ...
