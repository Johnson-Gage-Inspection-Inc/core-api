from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.create_employee_response_200 import (
    CreateEmployeeResponse200 as CreateEmployeeResponse200,
)
from ...models.qualer_api_models_clients_from_sponsored_employee_model import (
    QualerApiModelsClientsFromSponsoredEmployeeModel as QualerApiModelsClientsFromSponsoredEmployeeModel,
)
from ...models.qualer_api_models_clients_to_created_client_employee_response import (
    QualerApiModelsClientsToCreatedClientEmployeeResponse as QualerApiModelsClientsToCreatedClientEmployeeResponse,
)
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientsFromSponsoredEmployeeModel,
) -> Response[
    CreateEmployeeResponse200 | QualerApiModelsClientsToCreatedClientEmployeeResponse
]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientsFromSponsoredEmployeeModel,
) -> (
    CreateEmployeeResponse200
    | QualerApiModelsClientsToCreatedClientEmployeeResponse
    | None
): ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientsFromSponsoredEmployeeModel,
) -> Response[
    CreateEmployeeResponse200 | QualerApiModelsClientsToCreatedClientEmployeeResponse
]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientsFromSponsoredEmployeeModel,
) -> (
    CreateEmployeeResponse200
    | QualerApiModelsClientsToCreatedClientEmployeeResponse
    | None
): ...
