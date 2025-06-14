from uuid import UUID

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.post_response_200 import PostResponse200 as PostResponse200
from ...models.qualer_api_models_environment_from_environment_model import (
    QualerApiModelsEnvironmentFromEnvironmentModel as QualerApiModelsEnvironmentFromEnvironmentModel,
)
from ...types import Response as Response

def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEnvironmentFromEnvironmentModel,
) -> Response[PostResponse200]: ...
def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEnvironmentFromEnvironmentModel,
) -> PostResponse200 | None: ...
async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEnvironmentFromEnvironmentModel,
) -> Response[PostResponse200]: ...
async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsEnvironmentFromEnvironmentModel,
) -> PostResponse200 | None: ...
