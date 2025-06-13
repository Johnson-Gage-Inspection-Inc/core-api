from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_orders_to_service_order_task_response import (
    QualerApiModelsServiceOrdersToServiceOrderTaskResponse as QualerApiModelsServiceOrdersToServiceOrderTaskResponse,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[Any | list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]: ...
def sync(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Any | list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"] | None: ...
async def asyncio_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[Any | list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]: ...
async def asyncio(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Any | list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"] | None: ...
