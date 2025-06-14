from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_account_to_employee_event_message_response_model import (
    QualerApiModelsAccountToEmployeeEventMessageResponseModel as QualerApiModelsAccountToEmployeeEventMessageResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    message_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsAccountToEmployeeEventMessageResponseModel]: ...
def sync(
    message_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsAccountToEmployeeEventMessageResponseModel | None: ...
async def asyncio_detailed(
    message_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsAccountToEmployeeEventMessageResponseModel]: ...
async def asyncio(
    message_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsAccountToEmployeeEventMessageResponseModel | None: ...
