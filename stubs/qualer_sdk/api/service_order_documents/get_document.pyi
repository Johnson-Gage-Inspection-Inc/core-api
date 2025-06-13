from typing import Any
from uuid import UUID

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.get_document_response_200 import (
    GetDocumentResponse200 as GetDocumentResponse200,
)
from ...types import Response as Response

def sync_detailed(
    guid: UUID, *, client: AuthenticatedClient | Client
) -> Response[Any | GetDocumentResponse200]: ...
def sync(
    guid: UUID, *, client: AuthenticatedClient | Client
) -> Any | GetDocumentResponse200 | None: ...
async def asyncio_detailed(
    guid: UUID, *, client: AuthenticatedClient | Client
) -> Response[Any | GetDocumentResponse200]: ...
async def asyncio(
    guid: UUID, *, client: AuthenticatedClient | Client
) -> Any | GetDocumentResponse200 | None: ...
