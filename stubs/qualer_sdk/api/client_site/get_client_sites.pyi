from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_site_to_client_site_response import (
    QualerApiModelsSiteToClientSiteResponse as QualerApiModelsSiteToClientSiteResponse,
)
from ...types import Response as Response

def sync_detailed(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsSiteToClientSiteResponse"]]: ...
def sync(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsSiteToClientSiteResponse"] | None: ...
async def asyncio_detailed(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsSiteToClientSiteResponse"]]: ...
async def asyncio(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsSiteToClientSiteResponse"] | None: ...
