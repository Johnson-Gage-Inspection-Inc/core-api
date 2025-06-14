from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_company_to_sites_response_model import (
    QualerApiModelsCompanyToSitesResponseModel as QualerApiModelsCompanyToSitesResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsCompanyToSitesResponseModel"]]: ...
def sync(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsCompanyToSitesResponseModel"] | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsCompanyToSitesResponseModel"]]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsCompanyToSitesResponseModel"] | None: ...
