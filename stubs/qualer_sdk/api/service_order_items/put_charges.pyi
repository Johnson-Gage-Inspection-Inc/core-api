from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.put_charges_response_200 import (
    PutChargesResponse200 as PutChargesResponse200,
)
from ...models.qualer_api_models_service_orders_from_item_charge_update_model import (
    QualerApiModelsServiceOrdersFromItemChargeUpdateModel as QualerApiModelsServiceOrdersFromItemChargeUpdateModel,
)
from ...types import Response as Response

def sync_detailed(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromItemChargeUpdateModel,
) -> Response[PutChargesResponse200]: ...
def sync(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromItemChargeUpdateModel,
) -> PutChargesResponse200 | None: ...
async def asyncio_detailed(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromItemChargeUpdateModel,
) -> Response[PutChargesResponse200]: ...
async def asyncio(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromItemChargeUpdateModel,
) -> PutChargesResponse200 | None: ...
