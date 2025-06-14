from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_web_mvc_areas_api_models_company_from_update_department_model import (
    QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel as QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel,
)
from ...models.update_department_response_204 import (
    UpdateDepartmentResponse204 as UpdateDepartmentResponse204,
)
from ...types import Response as Response

def sync_detailed(
    department_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel,
) -> Response[Any | UpdateDepartmentResponse204]: ...
def sync(
    department_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel,
) -> Any | UpdateDepartmentResponse204 | None: ...
async def asyncio_detailed(
    department_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel,
) -> Response[Any | UpdateDepartmentResponse204]: ...
async def asyncio(
    department_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel,
) -> Any | UpdateDepartmentResponse204 | None: ...
