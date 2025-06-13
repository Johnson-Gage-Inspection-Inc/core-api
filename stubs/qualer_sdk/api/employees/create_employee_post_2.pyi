from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_employees_from_create_employee_model import (
    QualerApiModelsEmployeesFromCreateEmployeeModel as QualerApiModelsEmployeesFromCreateEmployeeModel,
)
from ...models.qualer_api_models_employees_to_created_employee_response import (
    QualerApiModelsEmployeesToCreatedEmployeeResponse as QualerApiModelsEmployeesToCreatedEmployeeResponse,
)
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEmployeesFromCreateEmployeeModel,
) -> Response[Any | QualerApiModelsEmployeesToCreatedEmployeeResponse]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEmployeesFromCreateEmployeeModel,
) -> Any | QualerApiModelsEmployeesToCreatedEmployeeResponse | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEmployeesFromCreateEmployeeModel,
) -> Response[Any | QualerApiModelsEmployeesToCreatedEmployeeResponse]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEmployeesFromCreateEmployeeModel,
) -> Any | QualerApiModelsEmployeesToCreatedEmployeeResponse | None: ...
