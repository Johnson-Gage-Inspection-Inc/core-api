from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_report_datasets_to_measurement_chart_response import (
    QualerApiModelsReportDatasetsToMeasurementChartResponse as QualerApiModelsReportDatasetsToMeasurementChartResponse,
)
from ...types import Response as Response

def sync_detailed(
    service_order_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReportDatasetsToMeasurementChartResponse"]]: ...
def sync(
    service_order_item_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReportDatasetsToMeasurementChartResponse"] | None: ...
async def asyncio_detailed(
    service_order_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReportDatasetsToMeasurementChartResponse"]]: ...
async def asyncio(
    service_order_item_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReportDatasetsToMeasurementChartResponse"] | None: ...
