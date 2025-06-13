from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_from_update_asset_class_model import (
    QualerApiModelsAssetFromUpdateAssetClassModel as QualerApiModelsAssetFromUpdateAssetClassModel,
)
from ...models.update_asset_class_response_200 import (
    UpdateAssetClassResponse200 as UpdateAssetClassResponse200,
)
from ...types import Response as Response

def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateAssetClassModel,
) -> Response[UpdateAssetClassResponse200]: ...
def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateAssetClassModel,
) -> UpdateAssetClassResponse200 | None: ...
async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateAssetClassModel,
) -> Response[UpdateAssetClassResponse200]: ...
async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateAssetClassModel,
) -> UpdateAssetClassResponse200 | None: ...
