from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.add_product_response_200 import (
    AddProductResponse200 as AddProductResponse200,
)
from ...models.qualer_web_mvc_areas_api_models_product_from_product_api_edit_model import (
    QualerWebMvcAreasApiModelsProductFromProductApiEditModel as QualerWebMvcAreasApiModelsProductFromProductApiEditModel,
)
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsProductFromProductApiEditModel,
) -> Response[AddProductResponse200]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsProductFromProductApiEditModel,
) -> AddProductResponse200 | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsProductFromProductApiEditModel,
) -> Response[AddProductResponse200]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsProductFromProductApiEditModel,
) -> AddProductResponse200 | None: ...
