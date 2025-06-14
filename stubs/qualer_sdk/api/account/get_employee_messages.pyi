from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_account_to_employee_event_response_model import (
    QualerApiModelsAccountToEmployeeEventResponseModel as QualerApiModelsAccountToEmployeeEventResponseModel,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    model_period: Unset | int = ...,
    model_site_id: Unset | int = ...,
) -> Response[list["QualerApiModelsAccountToEmployeeEventResponseModel"]]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    model_period: Unset | int = ...,
    model_site_id: Unset | int = ...,
) -> list["QualerApiModelsAccountToEmployeeEventResponseModel"] | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    model_period: Unset | int = ...,
    model_site_id: Unset | int = ...,
) -> Response[list["QualerApiModelsAccountToEmployeeEventResponseModel"]]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    model_period: Unset | int = ...,
    model_site_id: Unset | int = ...,
) -> list["QualerApiModelsAccountToEmployeeEventResponseModel"] | None: ...
