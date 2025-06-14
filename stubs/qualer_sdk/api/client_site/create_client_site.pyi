from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.create_client_site_response_200 import (
    CreateClientSiteResponse200 as CreateClientSiteResponse200,
)
from ...models.qualer_api_models_site_from_site_create_model import (
    QualerApiModelsSiteFromSiteCreateModel as QualerApiModelsSiteFromSiteCreateModel,
)
from ...types import Response as Response

def sync_detailed(
    client_company_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsSiteFromSiteCreateModel,
) -> Response[Any | CreateClientSiteResponse200]: ...
def sync(
    client_company_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsSiteFromSiteCreateModel,
) -> Any | CreateClientSiteResponse200 | None: ...
async def asyncio_detailed(
    client_company_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsSiteFromSiteCreateModel,
) -> Response[Any | CreateClientSiteResponse200]: ...
async def asyncio(
    client_company_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsSiteFromSiteCreateModel,
) -> Any | CreateClientSiteResponse200 | None: ...
