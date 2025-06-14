from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_clients_to_client_company_response_model import (
    QualerApiModelsClientsToClientCompanyResponseModel as QualerApiModelsClientsToClientCompanyResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsClientsToClientCompanyResponseModel]: ...
def sync(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsClientsToClientCompanyResponseModel | None: ...
async def asyncio_detailed(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsClientsToClientCompanyResponseModel]: ...
async def asyncio(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsClientsToClientCompanyResponseModel | None: ...
