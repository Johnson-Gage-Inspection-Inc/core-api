from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.change_work_order_payment_status_response_200 import (
    ChangeWorkOrderPaymentStatusResponse200 as ChangeWorkOrderPaymentStatusResponse200,
)
from ...models.qualer_api_models_service_orders_from_update_payment_status_model import (
    QualerApiModelsServiceOrdersFromUpdatePaymentStatusModel as QualerApiModelsServiceOrdersFromUpdatePaymentStatusModel,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromUpdatePaymentStatusModel,
) -> Response[ChangeWorkOrderPaymentStatusResponse200]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromUpdatePaymentStatusModel,
) -> ChangeWorkOrderPaymentStatusResponse200 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromUpdatePaymentStatusModel,
) -> Response[ChangeWorkOrderPaymentStatusResponse200]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromUpdatePaymentStatusModel,
) -> ChangeWorkOrderPaymentStatusResponse200 | None: ...
