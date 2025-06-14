from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_orders_to_service_order_task_response import (
    QualerApiModelsServiceOrdersToServiceOrderTaskResponse as QualerApiModelsServiceOrdersToServiceOrderTaskResponse,
)
from ...models.qualer_web_mvc_areas_api_models_service_prices_from_service_price_bulk_edit_model import (
    QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel as QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel,
)
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel"],
) -> Response[list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel"],
) -> list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"] | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel"],
) -> Response[list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel"],
) -> list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"] | None: ...
