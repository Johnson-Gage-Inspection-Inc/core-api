from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_clients_from_sponsored_client_create_model import (
    QualerApiModelsClientsFromSponsoredClientCreateModel as QualerApiModelsClientsFromSponsoredClientCreateModel,
)
from ...models.qualer_api_models_clients_to_created_client_company_response import (
    QualerApiModelsClientsToCreatedClientCompanyResponse as QualerApiModelsClientsToCreatedClientCompanyResponse,
)
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientsFromSponsoredClientCreateModel,
) -> Response[Any | QualerApiModelsClientsToCreatedClientCompanyResponse]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientsFromSponsoredClientCreateModel,
) -> Any | QualerApiModelsClientsToCreatedClientCompanyResponse | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientsFromSponsoredClientCreateModel,
) -> Response[Any | QualerApiModelsClientsToCreatedClientCompanyResponse]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientsFromSponsoredClientCreateModel,
) -> Any | QualerApiModelsClientsToCreatedClientCompanyResponse | None: ...
