from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_orders_to_client_order_item_response_model import (
    QualerApiModelsServiceOrdersToClientOrderItemResponseModel as QualerApiModelsServiceOrdersToClientOrderItemResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsServiceOrdersToClientOrderItemResponseModel]: ...
def sync(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsServiceOrdersToClientOrderItemResponseModel | None: ...
async def asyncio_detailed(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsServiceOrdersToClientOrderItemResponseModel]: ...
async def asyncio(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsServiceOrdersToClientOrderItemResponseModel | None: ...
