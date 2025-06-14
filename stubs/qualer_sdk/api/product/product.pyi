from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.product_response_200 import ProductResponse200 as ProductResponse200
from ...models.qualer_web_mvc_areas_api_models_product_from_product_api_edit_model import (
    QualerWebMvcAreasApiModelsProductFromProductApiEditModel as QualerWebMvcAreasApiModelsProductFromProductApiEditModel,
)
from ...types import Response as Response

def sync_detailed(
    product_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsProductFromProductApiEditModel,
) -> Response[ProductResponse200]: ...
def sync(
    product_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsProductFromProductApiEditModel,
) -> ProductResponse200 | None: ...
async def asyncio_detailed(
    product_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsProductFromProductApiEditModel,
) -> Response[ProductResponse200]: ...
async def asyncio(
    product_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsProductFromProductApiEditModel,
) -> ProductResponse200 | None: ...
