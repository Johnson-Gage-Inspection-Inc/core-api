from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_orders_from_update_shipment_status_model import (
    QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel as QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel,
)
from ...models.update_shipment_status_response_200 import (
    UpdateShipmentStatusResponse200 as UpdateShipmentStatusResponse200,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel,
) -> Response[UpdateShipmentStatusResponse200]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel,
) -> UpdateShipmentStatusResponse200 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel,
) -> Response[UpdateShipmentStatusResponse200]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel,
) -> UpdateShipmentStatusResponse200 | None: ...
