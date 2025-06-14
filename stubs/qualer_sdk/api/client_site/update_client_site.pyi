from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_site_from_site_update_model import (
    QualerApiModelsSiteFromSiteUpdateModel as QualerApiModelsSiteFromSiteUpdateModel,
)
from ...models.update_client_site_response_200 import (
    UpdateClientSiteResponse200 as UpdateClientSiteResponse200,
)
from ...types import Response as Response

def sync_detailed(
    client_company_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsSiteFromSiteUpdateModel,
) -> Response[Any | UpdateClientSiteResponse200]: ...
def sync(
    client_company_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsSiteFromSiteUpdateModel,
) -> Any | UpdateClientSiteResponse200 | None: ...
async def asyncio_detailed(
    client_company_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsSiteFromSiteUpdateModel,
) -> Response[Any | UpdateClientSiteResponse200]: ...
async def asyncio(
    client_company_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsSiteFromSiteUpdateModel,
) -> Any | UpdateClientSiteResponse200 | None: ...
