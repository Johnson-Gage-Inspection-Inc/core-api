from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.change_order_status_response_200 import (
    ChangeOrderStatusResponse200 as ChangeOrderStatusResponse200,
)
from ...models.qualer_api_models_service_orders_from_change_service_order_status_model import (
    QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel as QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel,
) -> Response[Any | ChangeOrderStatusResponse200]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel,
) -> Any | ChangeOrderStatusResponse200 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel,
) -> Response[Any | ChangeOrderStatusResponse200]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel,
) -> Any | ChangeOrderStatusResponse200 | None: ...
