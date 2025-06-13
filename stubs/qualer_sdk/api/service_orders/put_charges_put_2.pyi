from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.put_charges_put_2_response_200 import (
    PutChargesPut2Response200 as PutChargesPut2Response200,
)
from ...models.qualer_api_models_service_orders_from_charge_update_model import (
    QualerApiModelsServiceOrdersFromChargeUpdateModel as QualerApiModelsServiceOrdersFromChargeUpdateModel,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromChargeUpdateModel,
) -> Response[PutChargesPut2Response200]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromChargeUpdateModel,
) -> PutChargesPut2Response200 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromChargeUpdateModel,
) -> Response[PutChargesPut2Response200]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromChargeUpdateModel,
) -> PutChargesPut2Response200 | None: ...
