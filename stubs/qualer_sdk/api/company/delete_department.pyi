from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.delete_department_response_204 import (
    DeleteDepartmentResponse204 as DeleteDepartmentResponse204,
)
from ...types import Response as Response

def sync_detailed(
    department_id: int, *, client: AuthenticatedClient | Client
) -> Response[Any | DeleteDepartmentResponse204]: ...
def sync(
    department_id: int, *, client: AuthenticatedClient | Client
) -> Any | DeleteDepartmentResponse204 | None: ...
async def asyncio_detailed(
    department_id: int, *, client: AuthenticatedClient | Client
) -> Response[Any | DeleteDepartmentResponse204]: ...
async def asyncio(
    department_id: int, *, client: AuthenticatedClient | Client
) -> Any | DeleteDepartmentResponse204 | None: ...
