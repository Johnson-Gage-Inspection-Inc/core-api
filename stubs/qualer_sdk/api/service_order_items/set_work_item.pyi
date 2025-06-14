from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_orders_from_order_item_update_model import (
    QualerApiModelsServiceOrdersFromOrderItemUpdateModel as QualerApiModelsServiceOrdersFromOrderItemUpdateModel,
)
from ...models.set_work_item_response_200 import (
    SetWorkItemResponse200 as SetWorkItemResponse200,
)
from ...types import Response as Response

def sync_detailed(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromOrderItemUpdateModel,
) -> Response[Any | SetWorkItemResponse200]: ...
def sync(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromOrderItemUpdateModel,
) -> Any | SetWorkItemResponse200 | None: ...
async def asyncio_detailed(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromOrderItemUpdateModel,
) -> Response[Any | SetWorkItemResponse200]: ...
async def asyncio(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromOrderItemUpdateModel,
) -> Any | SetWorkItemResponse200 | None: ...
