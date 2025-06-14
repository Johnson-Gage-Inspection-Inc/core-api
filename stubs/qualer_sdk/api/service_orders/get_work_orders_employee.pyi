from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_orders_to_provider_service_order_response_model import (
    QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel as QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    employee_id: int,
    *,
    client: AuthenticatedClient | Client,
    is_internal: Unset | bool = ...,
) -> Response[
    list["QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel"]
]: ...
def sync(
    employee_id: int,
    *,
    client: AuthenticatedClient | Client,
    is_internal: Unset | bool = ...,
) -> list["QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel"] | None: ...
async def asyncio_detailed(
    employee_id: int,
    *,
    client: AuthenticatedClient | Client,
    is_internal: Unset | bool = ...,
) -> Response[
    list["QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel"]
]: ...
async def asyncio(
    employee_id: int,
    *,
    client: AuthenticatedClient | Client,
    is_internal: Unset | bool = ...,
) -> list["QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel"] | None: ...
