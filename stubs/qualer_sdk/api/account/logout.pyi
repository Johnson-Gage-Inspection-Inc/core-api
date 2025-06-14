from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.logout_response_200 import LogoutResponse200 as LogoutResponse200
from ...models.qualer_api_models_account_to_logout_model import (
    QualerApiModelsAccountToLogoutModel as QualerApiModelsAccountToLogoutModel,
)
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client, body: QualerApiModelsAccountToLogoutModel
) -> Response[Any | LogoutResponse200]: ...
def sync(
    *, client: AuthenticatedClient | Client, body: QualerApiModelsAccountToLogoutModel
) -> Any | LogoutResponse200 | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client, body: QualerApiModelsAccountToLogoutModel
) -> Response[Any | LogoutResponse200]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client, body: QualerApiModelsAccountToLogoutModel
) -> Any | LogoutResponse200 | None: ...
