from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_report_datasets_to_service_order_response import (
    QualerApiModelsReportDatasetsToServiceOrderResponse as QualerApiModelsReportDatasetsToServiceOrderResponse,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsReportDatasetsToServiceOrderResponse]: ...
def sync(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsReportDatasetsToServiceOrderResponse | None: ...
async def asyncio_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsReportDatasetsToServiceOrderResponse]: ...
async def asyncio(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsReportDatasetsToServiceOrderResponse | None: ...
