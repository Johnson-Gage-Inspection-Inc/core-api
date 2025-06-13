from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.create_asset_response_200 import (
    CreateAssetResponse200 as CreateAssetResponse200,
)
from ...models.qualer_api_models_clients_from_asset_model import (
    QualerApiModelsClientsFromAssetModel as QualerApiModelsClientsFromAssetModel,
)
from ...models.qualer_api_models_clients_to_created_client_asset_response import (
    QualerApiModelsClientsToCreatedClientAssetResponse as QualerApiModelsClientsToCreatedClientAssetResponse,
)
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client, body: QualerApiModelsClientsFromAssetModel
) -> Response[
    CreateAssetResponse200 | QualerApiModelsClientsToCreatedClientAssetResponse
]: ...
def sync(
    *, client: AuthenticatedClient | Client, body: QualerApiModelsClientsFromAssetModel
) -> (
    CreateAssetResponse200 | QualerApiModelsClientsToCreatedClientAssetResponse | None
): ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client, body: QualerApiModelsClientsFromAssetModel
) -> Response[
    CreateAssetResponse200 | QualerApiModelsClientsToCreatedClientAssetResponse
]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client, body: QualerApiModelsClientsFromAssetModel
) -> (
    CreateAssetResponse200 | QualerApiModelsClientsToCreatedClientAssetResponse | None
): ...
