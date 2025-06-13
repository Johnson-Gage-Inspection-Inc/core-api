from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.add_employee_department_response_204 import (
    AddEmployeeDepartmentResponse204 as AddEmployeeDepartmentResponse204,
)
from ...models.qualer_api_models_employees_from_employee_department_model import (
    QualerApiModelsEmployeesFromEmployeeDepartmentModel as QualerApiModelsEmployeesFromEmployeeDepartmentModel,
)
from ...types import Response as Response

def sync_detailed(
    employee_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEmployeesFromEmployeeDepartmentModel,
) -> Response[AddEmployeeDepartmentResponse204 | Any]: ...
def sync(
    employee_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEmployeesFromEmployeeDepartmentModel,
) -> AddEmployeeDepartmentResponse204 | Any | None: ...
async def asyncio_detailed(
    employee_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEmployeesFromEmployeeDepartmentModel,
) -> Response[AddEmployeeDepartmentResponse204 | Any]: ...
async def asyncio(
    employee_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEmployeesFromEmployeeDepartmentModel,
) -> AddEmployeeDepartmentResponse204 | Any | None: ...
