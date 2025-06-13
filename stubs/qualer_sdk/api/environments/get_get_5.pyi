from uuid import UUID

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_environment_to_environment_model import (
    QualerApiModelsEnvironmentToEnvironmentModel as QualerApiModelsEnvironmentToEnvironmentModel,
)
from ...types import Response as Response

def sync_detailed(
    id: UUID, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsEnvironmentToEnvironmentModel"]]: ...
def sync(
    id: UUID, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsEnvironmentToEnvironmentModel"] | None: ...
async def asyncio_detailed(
    id: UUID, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsEnvironmentToEnvironmentModel"]]: ...
async def asyncio(
    id: UUID, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsEnvironmentToEnvironmentModel"] | None: ...
