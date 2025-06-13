from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.create_work_item_task_response_200 import (
    CreateWorkItemTaskResponse200 as CreateWorkItemTaskResponse200,
)
from ...models.qualer_api_models_service_order_item_tasks_from_service_order_item_task_create_model import (
    QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel as QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel,
)
from ...types import Response as Response

def sync_detailed(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel,
) -> Response[CreateWorkItemTaskResponse200]: ...
def sync(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel,
) -> CreateWorkItemTaskResponse200 | None: ...
async def asyncio_detailed(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel,
) -> Response[CreateWorkItemTaskResponse200]: ...
async def asyncio(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel,
) -> CreateWorkItemTaskResponse200 | None: ...
