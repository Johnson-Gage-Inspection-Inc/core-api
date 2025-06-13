from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.create_async_response_201 import (
    CreateAsyncResponse201 as CreateAsyncResponse201,
)
from ...models.qualer_api_models_service_orders_from_create_order_model import (
    QualerApiModelsServiceOrdersFromCreateOrderModel as QualerApiModelsServiceOrdersFromCreateOrderModel,
)
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromCreateOrderModel,
) -> Response[Any | CreateAsyncResponse201]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromCreateOrderModel,
) -> Any | CreateAsyncResponse201 | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromCreateOrderModel,
) -> Response[Any | CreateAsyncResponse201]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromCreateOrderModel,
) -> Any | CreateAsyncResponse201 | None: ...
