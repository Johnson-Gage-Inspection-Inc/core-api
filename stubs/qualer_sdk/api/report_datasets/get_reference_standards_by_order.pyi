from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_report_datasets_to_reference_standard_response import (
    QualerApiModelsReportDatasetsToReferenceStandardResponse as QualerApiModelsReportDatasetsToReferenceStandardResponse,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReportDatasetsToReferenceStandardResponse"]]: ...
def sync(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReportDatasetsToReferenceStandardResponse"] | None: ...
async def asyncio_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReportDatasetsToReferenceStandardResponse"]]: ...
async def asyncio(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReportDatasetsToReferenceStandardResponse"] | None: ...
