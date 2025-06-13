from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_clients_from_sponsored_client_edit_model import (
    QualerApiModelsClientsFromSponsoredClientEditModel as QualerApiModelsClientsFromSponsoredClientEditModel,
)
from ...models.update_response_200 import UpdateResponse200 as UpdateResponse200
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientsFromSponsoredClientEditModel,
) -> Response[Any | UpdateResponse200]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientsFromSponsoredClientEditModel,
) -> Any | UpdateResponse200 | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientsFromSponsoredClientEditModel,
) -> Response[Any | UpdateResponse200]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientsFromSponsoredClientEditModel,
) -> Any | UpdateResponse200 | None: ...
