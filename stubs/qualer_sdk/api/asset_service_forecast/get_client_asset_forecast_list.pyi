from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_to_asset_service_forecast_model import (
    QualerApiModelsAssetToAssetServiceForecastModel as QualerApiModelsAssetToAssetServiceForecastModel,
)
from ...types import Response as Response

def sync_detailed(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsAssetToAssetServiceForecastModel"]]: ...
def sync(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsAssetToAssetServiceForecastModel"] | None: ...
async def asyncio_detailed(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsAssetToAssetServiceForecastModel"]]: ...
async def asyncio(
    client_company_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsAssetToAssetServiceForecastModel"] | None: ...
