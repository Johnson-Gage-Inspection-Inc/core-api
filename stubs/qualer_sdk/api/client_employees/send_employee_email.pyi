from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_clients_from_send_employee_email_model import (
    QualerApiModelsClientsFromSendEmployeeEmailModel as QualerApiModelsClientsFromSendEmployeeEmailModel,
)
from ...models.send_employee_email_response_200 import (
    SendEmployeeEmailResponse200 as SendEmployeeEmailResponse200,
)
from ...types import Response as Response

def sync_detailed(
    employee_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientsFromSendEmployeeEmailModel,
) -> Response[SendEmployeeEmailResponse200]: ...
def sync(
    employee_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientsFromSendEmployeeEmailModel,
) -> SendEmployeeEmailResponse200 | None: ...
async def asyncio_detailed(
    employee_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientsFromSendEmployeeEmailModel,
) -> Response[SendEmployeeEmailResponse200]: ...
async def asyncio(
    employee_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientsFromSendEmployeeEmailModel,
) -> SendEmployeeEmailResponse200 | None: ...
