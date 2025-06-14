from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_web_mvc_areas_api_models_service_orders_from_service_order_part_repair_update_model import (
    QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairUpdateModel as QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairUpdateModel,
)
from ...models.update_work_order_parts_response_204 import (
    UpdateWorkOrderPartsResponse204 as UpdateWorkOrderPartsResponse204,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairUpdateModel,
) -> Response[Any | UpdateWorkOrderPartsResponse204]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairUpdateModel,
) -> Any | UpdateWorkOrderPartsResponse204 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairUpdateModel,
) -> Response[Any | UpdateWorkOrderPartsResponse204]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairUpdateModel,
) -> Any | UpdateWorkOrderPartsResponse204 | None: ...
