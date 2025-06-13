from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.create_work_order_task_response_204 import (
    CreateWorkOrderTaskResponse204 as CreateWorkOrderTaskResponse204,
)
from ...models.qualer_api_models_service_orders_from_service_order_task_create_model import (
    QualerApiModelsServiceOrdersFromServiceOrderTaskCreateModel as QualerApiModelsServiceOrdersFromServiceOrderTaskCreateModel,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromServiceOrderTaskCreateModel,
) -> Response[Any | CreateWorkOrderTaskResponse204]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromServiceOrderTaskCreateModel,
) -> Any | CreateWorkOrderTaskResponse204 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromServiceOrderTaskCreateModel,
) -> Response[Any | CreateWorkOrderTaskResponse204]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromServiceOrderTaskCreateModel,
) -> Any | CreateWorkOrderTaskResponse204 | None: ...
