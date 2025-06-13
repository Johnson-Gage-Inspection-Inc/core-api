from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_report_datasets_to_external_data_report_response import (
    QualerApiModelsReportDatasetsToExternalDataReportResponse as QualerApiModelsReportDatasetsToExternalDataReportResponse,
)
from ...types import UNSET as UNSET
from ...types import Response as Response

def sync_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    service_order_item_ids: list[int],
) -> Response[list["QualerApiModelsReportDatasetsToExternalDataReportResponse"]]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    service_order_item_ids: list[int],
) -> list["QualerApiModelsReportDatasetsToExternalDataReportResponse"] | None: ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    service_order_item_ids: list[int],
) -> Response[list["QualerApiModelsReportDatasetsToExternalDataReportResponse"]]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    service_order_item_ids: list[int],
) -> list["QualerApiModelsReportDatasetsToExternalDataReportResponse"] | None: ...
