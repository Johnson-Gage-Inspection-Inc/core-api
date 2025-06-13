from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_account_from_login_response_model import (
    QualerApiModelsAccountFromLoginResponseModel as QualerApiModelsAccountFromLoginResponseModel,
)
from ...models.qualer_web_mvc_areas_api_models_account_to_login_model import (
    QualerWebMvcAreasApiModelsAccountToLoginModel as QualerWebMvcAreasApiModelsAccountToLoginModel,
)
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsAccountToLoginModel,
) -> Response[Any | QualerApiModelsAccountFromLoginResponseModel]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsAccountToLoginModel,
) -> Any | QualerApiModelsAccountFromLoginResponseModel | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsAccountToLoginModel,
) -> Response[Any | QualerApiModelsAccountFromLoginResponseModel]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsAccountToLoginModel,
) -> Any | QualerApiModelsAccountFromLoginResponseModel | None: ...
