from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_report_datasets_to_measurement_field_response import (
    QualerApiModelsReportDatasetsToMeasurementFieldResponse as QualerApiModelsReportDatasetsToMeasurementFieldResponse,
)
from ...types import Response as Response

def sync_detailed(
    service_order_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReportDatasetsToMeasurementFieldResponse"]]: ...
def sync(
    service_order_item_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReportDatasetsToMeasurementFieldResponse"] | None: ...
async def asyncio_detailed(
    service_order_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReportDatasetsToMeasurementFieldResponse"]]: ...
async def asyncio(
    service_order_item_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReportDatasetsToMeasurementFieldResponse"] | None: ...
