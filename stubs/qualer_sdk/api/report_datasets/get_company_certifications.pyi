from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_report_datasets_to_company_certification_response import (
    QualerApiModelsReportDatasetsToCompanyCertificationResponse as QualerApiModelsReportDatasetsToCompanyCertificationResponse,
)
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReportDatasetsToCompanyCertificationResponse"]]: ...
def sync(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReportDatasetsToCompanyCertificationResponse"] | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReportDatasetsToCompanyCertificationResponse"]]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReportDatasetsToCompanyCertificationResponse"] | None: ...
