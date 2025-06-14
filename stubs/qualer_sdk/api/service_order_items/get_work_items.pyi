from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_orders_to_client_order_item_response_model import (
    QualerApiModelsServiceOrdersToClientOrderItemResponseModel as QualerApiModelsServiceOrdersToClientOrderItemResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsServiceOrdersToClientOrderItemResponseModel"]]: ...
def sync(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsServiceOrdersToClientOrderItemResponseModel"] | None: ...
async def asyncio_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsServiceOrdersToClientOrderItemResponseModel"]]: ...
async def asyncio(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsServiceOrdersToClientOrderItemResponseModel"] | None: ...
