from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_company_to_environment_response_model import (
    QualerApiModelsCompanyToEnvironmentResponseModel as QualerApiModelsCompanyToEnvironmentResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    id: int, *, client: AuthenticatedClient | Client
) -> Response[Any | list["QualerApiModelsCompanyToEnvironmentResponseModel"]]: ...
def sync(
    id: int, *, client: AuthenticatedClient | Client
) -> Any | list["QualerApiModelsCompanyToEnvironmentResponseModel"] | None: ...
async def asyncio_detailed(
    id: int, *, client: AuthenticatedClient | Client
) -> Response[Any | list["QualerApiModelsCompanyToEnvironmentResponseModel"]]: ...
async def asyncio(
    id: int, *, client: AuthenticatedClient | Client
) -> Any | list["QualerApiModelsCompanyToEnvironmentResponseModel"] | None: ...
