from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_orders_from_add_work_items_model import (
    QualerApiModelsServiceOrdersFromAddWorkItemsModel as QualerApiModelsServiceOrdersFromAddWorkItemsModel,
)
from ...models.qualer_api_models_service_orders_to_asset_add_result_response_model import (
    QualerApiModelsServiceOrdersToAssetAddResultResponseModel as QualerApiModelsServiceOrdersToAssetAddResultResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromAddWorkItemsModel,
) -> Response[Any | QualerApiModelsServiceOrdersToAssetAddResultResponseModel]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromAddWorkItemsModel,
) -> Any | QualerApiModelsServiceOrdersToAssetAddResultResponseModel | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromAddWorkItemsModel,
) -> Response[Any | QualerApiModelsServiceOrdersToAssetAddResultResponseModel]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromAddWorkItemsModel,
) -> Any | QualerApiModelsServiceOrdersToAssetAddResultResponseModel | None: ...
