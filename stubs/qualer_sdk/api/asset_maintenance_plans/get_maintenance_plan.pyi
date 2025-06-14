from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_to_asset_maintenance_plan_model import (
    QualerApiModelsAssetToAssetMaintenancePlanModel as QualerApiModelsAssetToAssetMaintenancePlanModel,
)
from ...types import Response as Response

def sync_detailed(
    asset_id: int, maintenance_plan_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsAssetToAssetMaintenancePlanModel]: ...
def sync(
    asset_id: int, maintenance_plan_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsAssetToAssetMaintenancePlanModel | None: ...
async def asyncio_detailed(
    asset_id: int, maintenance_plan_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsAssetToAssetMaintenancePlanModel]: ...
async def asyncio(
    asset_id: int, maintenance_plan_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsAssetToAssetMaintenancePlanModel | None: ...
