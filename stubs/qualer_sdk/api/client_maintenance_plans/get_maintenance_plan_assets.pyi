from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_to_asset_forecast_api_response_model import (
    QualerApiModelsAssetToAssetForecastApiResponseModel as QualerApiModelsAssetToAssetForecastApiResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    maintenance_plan_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsAssetToAssetForecastApiResponseModel"]]: ...
def sync(
    maintenance_plan_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsAssetToAssetForecastApiResponseModel"] | None: ...
async def asyncio_detailed(
    maintenance_plan_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsAssetToAssetForecastApiResponseModel"]]: ...
async def asyncio(
    maintenance_plan_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsAssetToAssetForecastApiResponseModel"] | None: ...
