from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.delete_employee_department_response_204 import (
    DeleteEmployeeDepartmentResponse204 as DeleteEmployeeDepartmentResponse204,
)
from ...types import Response as Response

def sync_detailed(
    employee_id: int, department_id: int, *, client: AuthenticatedClient | Client
) -> Response[Any | DeleteEmployeeDepartmentResponse204]: ...
def sync(
    employee_id: int, department_id: int, *, client: AuthenticatedClient | Client
) -> Any | DeleteEmployeeDepartmentResponse204 | None: ...
async def asyncio_detailed(
    employee_id: int, department_id: int, *, client: AuthenticatedClient | Client
) -> Response[Any | DeleteEmployeeDepartmentResponse204]: ...
async def asyncio(
    employee_id: int, department_id: int, *, client: AuthenticatedClient | Client
) -> Any | DeleteEmployeeDepartmentResponse204 | None: ...
