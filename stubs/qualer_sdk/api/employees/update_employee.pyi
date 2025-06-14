from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_employees_from_update_employee_model import (
    QualerApiModelsEmployeesFromUpdateEmployeeModel as QualerApiModelsEmployeesFromUpdateEmployeeModel,
)
from ...models.update_employee_response_201 import (
    UpdateEmployeeResponse201 as UpdateEmployeeResponse201,
)
from ...types import Response as Response

def sync_detailed(
    employee_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEmployeesFromUpdateEmployeeModel,
) -> Response[Any | UpdateEmployeeResponse201]: ...
def sync(
    employee_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEmployeesFromUpdateEmployeeModel,
) -> Any | UpdateEmployeeResponse201 | None: ...
async def asyncio_detailed(
    employee_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEmployeesFromUpdateEmployeeModel,
) -> Response[Any | UpdateEmployeeResponse201]: ...
async def asyncio(
    employee_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEmployeesFromUpdateEmployeeModel,
) -> Any | UpdateEmployeeResponse201 | None: ...
