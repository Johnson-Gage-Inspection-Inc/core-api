from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_to_client_asset_counters_response_model import (
    QualerApiModelsAssetToClientAssetCountersResponseModel as QualerApiModelsAssetToClientAssetCountersResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsAssetToClientAssetCountersResponseModel]: ...
def sync(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsAssetToClientAssetCountersResponseModel | None: ...
async def asyncio_detailed(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsAssetToClientAssetCountersResponseModel]: ...
async def asyncio(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsAssetToClientAssetCountersResponseModel | None: ...
