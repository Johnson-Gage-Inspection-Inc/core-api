from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_clients_to_employee_response_model import (
    QualerApiModelsClientsToEmployeeResponseModel as QualerApiModelsClientsToEmployeeResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsClientsToEmployeeResponseModel"]]: ...
def sync(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsClientsToEmployeeResponseModel"] | None: ...
async def asyncio_detailed(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsClientsToEmployeeResponseModel"]]: ...
async def asyncio(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsClientsToEmployeeResponseModel"] | None: ...
