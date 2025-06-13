from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_orders_to_payment_response_model import (
    QualerApiModelsServiceOrdersToPaymentResponseModel as QualerApiModelsServiceOrdersToPaymentResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsServiceOrdersToPaymentResponseModel"]]: ...
def sync(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsServiceOrdersToPaymentResponseModel"] | None: ...
async def asyncio_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsServiceOrdersToPaymentResponseModel"]]: ...
async def asyncio(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsServiceOrdersToPaymentResponseModel"] | None: ...
