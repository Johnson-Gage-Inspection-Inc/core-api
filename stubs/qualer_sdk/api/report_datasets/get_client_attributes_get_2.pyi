from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_report_datasets_to_client_attribute_response import (
    QualerApiModelsReportDatasetsToClientAttributeResponse as QualerApiModelsReportDatasetsToClientAttributeResponse,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsReportDatasetsToClientAttributeResponse]: ...
def sync(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsReportDatasetsToClientAttributeResponse | None: ...
async def asyncio_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsReportDatasetsToClientAttributeResponse]: ...
async def asyncio(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsReportDatasetsToClientAttributeResponse | None: ...
