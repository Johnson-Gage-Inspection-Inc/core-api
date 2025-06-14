from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.append_shipment_tracking_number_response_200 import (
    AppendShipmentTrackingNumberResponse200 as AppendShipmentTrackingNumberResponse200,
)
from ...models.qualer_api_models_service_orders_from_append_tracking_number_model import (
    QualerApiModelsServiceOrdersFromAppendTrackingNumberModel as QualerApiModelsServiceOrdersFromAppendTrackingNumberModel,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromAppendTrackingNumberModel,
) -> Response[AppendShipmentTrackingNumberResponse200]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromAppendTrackingNumberModel,
) -> AppendShipmentTrackingNumberResponse200 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromAppendTrackingNumberModel,
) -> Response[AppendShipmentTrackingNumberResponse200]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromAppendTrackingNumberModel,
) -> AppendShipmentTrackingNumberResponse200 | None: ...
