from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_orders_from_add_payment_model import (
    QualerApiModelsServiceOrdersFromAddPaymentModel as QualerApiModelsServiceOrdersFromAddPaymentModel,
)
from ...models.qualer_api_models_service_orders_to_created_work_order_payment_response import (
    QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse as QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromAddPaymentModel,
) -> Response[QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromAddPaymentModel,
) -> QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromAddPaymentModel,
) -> Response[QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromAddPaymentModel,
) -> QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse | None: ...
