from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_report_datasets_to_measurement_channel_result_response import (
    QualerApiModelsReportDatasetsToMeasurementChannelResultResponse as QualerApiModelsReportDatasetsToMeasurementChannelResultResponse,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[
    list["QualerApiModelsReportDatasetsToMeasurementChannelResultResponse"]
]: ...
def sync(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReportDatasetsToMeasurementChannelResultResponse"] | None: ...
async def asyncio_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[
    list["QualerApiModelsReportDatasetsToMeasurementChannelResultResponse"]
]: ...
async def asyncio(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReportDatasetsToMeasurementChannelResultResponse"] | None: ...
