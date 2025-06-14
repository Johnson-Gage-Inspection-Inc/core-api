from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_from_update_asset_maintenance_service_dat import (
    QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat as QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat,
)
from ...models.reset_initial_service_date_response_200 import (
    ResetInitialServiceDateResponse200 as ResetInitialServiceDateResponse200,
)
from ...types import Response as Response

def sync_detailed(
    asset_id: int,
    maintenance_plan_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat,
) -> Response[ResetInitialServiceDateResponse200]: ...
def sync(
    asset_id: int,
    maintenance_plan_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat,
) -> ResetInitialServiceDateResponse200 | None: ...
async def asyncio_detailed(
    asset_id: int,
    maintenance_plan_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat,
) -> Response[ResetInitialServiceDateResponse200]: ...
async def asyncio(
    asset_id: int,
    maintenance_plan_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat,
) -> ResetInitialServiceDateResponse200 | None: ...
