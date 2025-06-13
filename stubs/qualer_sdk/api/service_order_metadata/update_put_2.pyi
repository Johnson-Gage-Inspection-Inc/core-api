from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_orders_from_service_order_metadata_update_model import (
    QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel as QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel,
)
from ...models.update_put_2_response_200 import (
    UpdatePut2Response200 as UpdatePut2Response200,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel,
) -> Response[UpdatePut2Response200]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel,
) -> UpdatePut2Response200 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel,
) -> Response[UpdatePut2Response200]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel,
) -> UpdatePut2Response200 | None: ...
