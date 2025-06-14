from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_orders_to_service_order_task_response import (
    QualerApiModelsServiceOrdersToServiceOrderTaskResponse as QualerApiModelsServiceOrdersToServiceOrderTaskResponse,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    service_pricing_id: int,
    service_group_id: Unset | int = ...,
) -> Response[list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    service_pricing_id: int,
    service_group_id: Unset | int = ...,
) -> list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"] | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    service_pricing_id: int,
    service_group_id: Unset | int = ...,
) -> Response[list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"]]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    service_pricing_id: int,
    service_group_id: Unset | int = ...,
) -> list["QualerApiModelsServiceOrdersToServiceOrderTaskResponse"] | None: ...
