from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_product_to_product_api_response_model import (
    QualerApiModelsProductToProductApiResponseModel as QualerApiModelsProductToProductApiResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    product_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsProductToProductApiResponseModel]: ...
def sync(
    product_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsProductToProductApiResponseModel | None: ...
async def asyncio_detailed(
    product_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsProductToProductApiResponseModel]: ...
async def asyncio(
    product_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsProductToProductApiResponseModel | None: ...
