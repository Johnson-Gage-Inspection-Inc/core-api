from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_clients_to_employee_response_model import (
    QualerApiModelsClientsToEmployeeResponseModel as QualerApiModelsClientsToEmployeeResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    employee_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsClientsToEmployeeResponseModel]: ...
def sync(
    employee_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsClientsToEmployeeResponseModel | None: ...
async def asyncio_detailed(
    employee_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsClientsToEmployeeResponseModel]: ...
async def asyncio(
    employee_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsClientsToEmployeeResponseModel | None: ...
