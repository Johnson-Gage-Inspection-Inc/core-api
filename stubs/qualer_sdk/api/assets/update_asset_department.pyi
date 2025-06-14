from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_from_update_asset_department_model import (
    QualerApiModelsAssetFromUpdateAssetDepartmentModel as QualerApiModelsAssetFromUpdateAssetDepartmentModel,
)
from ...models.update_asset_department_response_200 import (
    UpdateAssetDepartmentResponse200 as UpdateAssetDepartmentResponse200,
)
from ...types import Response as Response

def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateAssetDepartmentModel,
) -> Response[UpdateAssetDepartmentResponse200]: ...
def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateAssetDepartmentModel,
) -> UpdateAssetDepartmentResponse200 | None: ...
async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateAssetDepartmentModel,
) -> Response[UpdateAssetDepartmentResponse200]: ...
async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateAssetDepartmentModel,
) -> UpdateAssetDepartmentResponse200 | None: ...
