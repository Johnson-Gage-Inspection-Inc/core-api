from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_orders_to_client_order_response_model import (
    QualerApiModelsServiceOrdersToClientOrderResponseModel as QualerApiModelsServiceOrdersToClientOrderResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsServiceOrdersToClientOrderResponseModel]: ...
def sync(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsServiceOrdersToClientOrderResponseModel | None: ...
async def asyncio_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsServiceOrdersToClientOrderResponseModel]: ...
async def asyncio(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsServiceOrdersToClientOrderResponseModel | None: ...
