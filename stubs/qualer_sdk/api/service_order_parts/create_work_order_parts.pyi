from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.create_work_order_parts_response_204 import (
    CreateWorkOrderPartsResponse204 as CreateWorkOrderPartsResponse204,
)
from ...models.qualer_web_mvc_areas_api_models_service_orders_from_service_order_part_repair_create_model import (
    QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel as QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel,
) -> Response[Any | CreateWorkOrderPartsResponse204]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel,
) -> Any | CreateWorkOrderPartsResponse204 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel,
) -> Response[Any | CreateWorkOrderPartsResponse204]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel,
) -> Any | CreateWorkOrderPartsResponse204 | None: ...
