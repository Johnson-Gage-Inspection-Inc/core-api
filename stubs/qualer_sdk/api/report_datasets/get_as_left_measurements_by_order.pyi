from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_report_datasets_to_measurement_response import (
    QualerApiModelsReportDatasetsToMeasurementResponse as QualerApiModelsReportDatasetsToMeasurementResponse,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReportDatasetsToMeasurementResponse"]]: ...
def sync(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReportDatasetsToMeasurementResponse"] | None: ...
async def asyncio_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReportDatasetsToMeasurementResponse"]]: ...
async def asyncio(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReportDatasetsToMeasurementResponse"] | None: ...
