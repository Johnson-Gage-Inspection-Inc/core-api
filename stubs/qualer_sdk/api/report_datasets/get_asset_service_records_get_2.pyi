from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_report_datasets_to_asset_summary_response import (
    QualerApiModelsReportDatasetsToAssetSummaryResponse as QualerApiModelsReportDatasetsToAssetSummaryResponse,
)
from ...types import Response as Response

def sync_detailed(
    service_order_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsReportDatasetsToAssetSummaryResponse]: ...
def sync(
    service_order_item_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsReportDatasetsToAssetSummaryResponse | None: ...
async def asyncio_detailed(
    service_order_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsReportDatasetsToAssetSummaryResponse]: ...
async def asyncio(
    service_order_item_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsReportDatasetsToAssetSummaryResponse | None: ...
