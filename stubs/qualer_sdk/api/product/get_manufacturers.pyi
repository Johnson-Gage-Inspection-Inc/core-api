from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_product_to_manufacturer_response_model import (
    QualerApiModelsProductToManufacturerResponseModel as QualerApiModelsProductToManufacturerResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsProductToManufacturerResponseModel"]]: ...
def sync(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsProductToManufacturerResponseModel"] | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsProductToManufacturerResponseModel"]]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsProductToManufacturerResponseModel"] | None: ...
