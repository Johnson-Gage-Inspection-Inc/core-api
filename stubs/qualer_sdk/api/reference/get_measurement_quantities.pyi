from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_reference_to_measurement_quantity_response import (
    QualerApiModelsReferenceToMeasurementQuantityResponse as QualerApiModelsReferenceToMeasurementQuantityResponse,
)
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReferenceToMeasurementQuantityResponse"]]: ...
def sync(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReferenceToMeasurementQuantityResponse"] | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReferenceToMeasurementQuantityResponse"]]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReferenceToMeasurementQuantityResponse"] | None: ...
