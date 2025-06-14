from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_company_to_departments_response_model import (
    QualerApiModelsCompanyToDepartmentsResponseModel as QualerApiModelsCompanyToDepartmentsResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsCompanyToDepartmentsResponseModel"]]: ...
def sync(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsCompanyToDepartmentsResponseModel"] | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsCompanyToDepartmentsResponseModel"]]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsCompanyToDepartmentsResponseModel"] | None: ...
