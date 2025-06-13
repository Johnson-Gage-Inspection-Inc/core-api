import datetime
from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_orders_to_client_order_response_model import (
    QualerApiModelsServiceOrdersToClientOrderResponseModel as QualerApiModelsServiceOrdersToClientOrderResponseModel,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: Unset | str = ...,
    company_id: Unset | int = ...,
    from_: Unset | datetime.datetime = ...,
    to: Unset | datetime.datetime = ...,
    modified_after: Unset | datetime.datetime = ...,
    work_order_number: Unset | str = ...,
    assigned_employees: Unset | str = ...,
) -> Response[Any | list["QualerApiModelsServiceOrdersToClientOrderResponseModel"]]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    status: Unset | str = ...,
    company_id: Unset | int = ...,
    from_: Unset | datetime.datetime = ...,
    to: Unset | datetime.datetime = ...,
    modified_after: Unset | datetime.datetime = ...,
    work_order_number: Unset | str = ...,
    assigned_employees: Unset | str = ...,
) -> Any | list["QualerApiModelsServiceOrdersToClientOrderResponseModel"] | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: Unset | str = ...,
    company_id: Unset | int = ...,
    from_: Unset | datetime.datetime = ...,
    to: Unset | datetime.datetime = ...,
    modified_after: Unset | datetime.datetime = ...,
    work_order_number: Unset | str = ...,
    assigned_employees: Unset | str = ...,
) -> Response[Any | list["QualerApiModelsServiceOrdersToClientOrderResponseModel"]]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: Unset | str = ...,
    company_id: Unset | int = ...,
    from_: Unset | datetime.datetime = ...,
    to: Unset | datetime.datetime = ...,
    modified_after: Unset | datetime.datetime = ...,
    work_order_number: Unset | str = ...,
    assigned_employees: Unset | str = ...,
) -> Any | list["QualerApiModelsServiceOrdersToClientOrderResponseModel"] | None: ...
