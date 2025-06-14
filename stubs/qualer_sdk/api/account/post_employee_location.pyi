from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.post_employee_location_response_200 import (
    PostEmployeeLocationResponse200 as PostEmployeeLocationResponse200,
)
from ...models.qualer_api_models_employees_from_employee_location_model import (
    QualerApiModelsEmployeesFromEmployeeLocationModel as QualerApiModelsEmployeesFromEmployeeLocationModel,
)
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEmployeesFromEmployeeLocationModel,
) -> Response[PostEmployeeLocationResponse200]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEmployeesFromEmployeeLocationModel,
) -> PostEmployeeLocationResponse200 | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEmployeesFromEmployeeLocationModel,
) -> Response[PostEmployeeLocationResponse200]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEmployeesFromEmployeeLocationModel,
) -> PostEmployeeLocationResponse200 | None: ...
