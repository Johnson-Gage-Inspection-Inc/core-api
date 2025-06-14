from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_report_datasets_to_measurement_channel_uniformity_response import (
    QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse as QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[
    list["QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse"]
]: ...
def sync(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> (
    list["QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse"] | None
): ...
async def asyncio_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[
    list["QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse"]
]: ...
async def asyncio(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> (
    list["QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse"] | None
): ...
