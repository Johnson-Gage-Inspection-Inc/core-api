from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.create_post_2_response_200 import (
    CreatePost2Response200 as CreatePost2Response200,
)
from ...models.qualer_api_models_service_orders_from_service_order_metadata_create_model import (
    QualerApiModelsServiceOrdersFromServiceOrderMetadataCreateModel as QualerApiModelsServiceOrdersFromServiceOrderMetadataCreateModel,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromServiceOrderMetadataCreateModel,
) -> Response[CreatePost2Response200]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromServiceOrderMetadataCreateModel,
) -> CreatePost2Response200 | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromServiceOrderMetadataCreateModel,
) -> Response[CreatePost2Response200]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsServiceOrdersFromServiceOrderMetadataCreateModel,
) -> CreatePost2Response200 | None: ...
