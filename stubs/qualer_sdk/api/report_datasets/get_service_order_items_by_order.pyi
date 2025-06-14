from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_report_datasets_to_service_order_item_response import (
    QualerApiModelsReportDatasetsToServiceOrderItemResponse as QualerApiModelsReportDatasetsToServiceOrderItemResponse,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReportDatasetsToServiceOrderItemResponse"]]: ...
def sync(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReportDatasetsToServiceOrderItemResponse"] | None: ...
async def asyncio_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReportDatasetsToServiceOrderItemResponse"]]: ...
async def asyncio(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReportDatasetsToServiceOrderItemResponse"] | None: ...
