from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_reference_to_unit_of_measure_response import (
    QualerApiModelsReferenceToUnitOfMeasureResponse as QualerApiModelsReferenceToUnitOfMeasureResponse,
)
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReferenceToUnitOfMeasureResponse"]]: ...
def sync(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReferenceToUnitOfMeasureResponse"] | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReferenceToUnitOfMeasureResponse"]]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReferenceToUnitOfMeasureResponse"] | None: ...
