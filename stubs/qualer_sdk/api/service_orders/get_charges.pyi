from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_web_mvc_areas_api_models_service_orders_to_charge_response_model import (
    QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel as QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel]: ...
def sync(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel | None: ...
async def asyncio_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel]: ...
async def asyncio(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel | None: ...
