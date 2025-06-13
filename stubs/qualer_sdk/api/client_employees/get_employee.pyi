from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_clients_to_employee_response_model import (
    QualerApiModelsClientsToEmployeeResponseModel as QualerApiModelsClientsToEmployeeResponseModel,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    employee_id_path: str,
    *,
    client: AuthenticatedClient | Client,
    employee_id_query: Unset | str = ...,
    model_employee_id: Unset | int = ...,
) -> Response[QualerApiModelsClientsToEmployeeResponseModel]: ...
def sync(
    employee_id_path: str,
    *,
    client: AuthenticatedClient | Client,
    employee_id_query: Unset | str = ...,
    model_employee_id: Unset | int = ...,
) -> QualerApiModelsClientsToEmployeeResponseModel | None: ...
async def asyncio_detailed(
    employee_id_path: str,
    *,
    client: AuthenticatedClient | Client,
    employee_id_query: Unset | str = ...,
    model_employee_id: Unset | int = ...,
) -> Response[QualerApiModelsClientsToEmployeeResponseModel]: ...
async def asyncio(
    employee_id_path: str,
    *,
    client: AuthenticatedClient | Client,
    employee_id_query: Unset | str = ...,
    model_employee_id: Unset | int = ...,
) -> QualerApiModelsClientsToEmployeeResponseModel | None: ...
