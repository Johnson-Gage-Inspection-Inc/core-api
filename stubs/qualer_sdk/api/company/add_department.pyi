from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.add_department_response_204 import (
    AddDepartmentResponse204 as AddDepartmentResponse204,
)
from ...models.qualer_web_mvc_areas_api_models_company_from_add_department_model import (
    QualerWebMvcAreasApiModelsCompanyFromAddDepartmentModel as QualerWebMvcAreasApiModelsCompanyFromAddDepartmentModel,
)
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsCompanyFromAddDepartmentModel,
) -> Response[AddDepartmentResponse204 | Any]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsCompanyFromAddDepartmentModel,
) -> AddDepartmentResponse204 | Any | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsCompanyFromAddDepartmentModel,
) -> Response[AddDepartmentResponse204 | Any]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsCompanyFromAddDepartmentModel,
) -> AddDepartmentResponse204 | Any | None: ...
