from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.companies_response_200 import (
    CompaniesResponse200 as CompaniesResponse200,
)
from ...models.qualer_web_mvc_areas_api_models_account_to_login_model import (
    QualerWebMvcAreasApiModelsAccountToLoginModel as QualerWebMvcAreasApiModelsAccountToLoginModel,
)
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsAccountToLoginModel,
) -> Response[CompaniesResponse200]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsAccountToLoginModel,
) -> CompaniesResponse200 | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsAccountToLoginModel,
) -> Response[CompaniesResponse200]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsAccountToLoginModel,
) -> CompaniesResponse200 | None: ...
