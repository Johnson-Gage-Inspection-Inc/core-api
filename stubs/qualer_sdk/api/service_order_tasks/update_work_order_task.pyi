from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_orders_from_service_order_task_update_model import (
    QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel as QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel,
)
from ...models.update_work_order_task_response_204 import (
    UpdateWorkOrderTaskResponse204 as UpdateWorkOrderTaskResponse204,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel,
) -> Response[Any | UpdateWorkOrderTaskResponse204]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel,
) -> Any | UpdateWorkOrderTaskResponse204 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel,
) -> Response[Any | UpdateWorkOrderTaskResponse204]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel,
) -> Any | UpdateWorkOrderTaskResponse204 | None: ...
