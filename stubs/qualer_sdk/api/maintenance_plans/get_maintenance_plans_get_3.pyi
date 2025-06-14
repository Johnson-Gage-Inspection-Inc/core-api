from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_maintenance_plans_to_maintenance_plan_response import (
    QualerApiModelsMaintenancePlansToMaintenancePlanResponse as QualerApiModelsMaintenancePlansToMaintenancePlanResponse,
)
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsMaintenancePlansToMaintenancePlanResponse"]]: ...
def sync(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsMaintenancePlansToMaintenancePlanResponse"] | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsMaintenancePlansToMaintenancePlanResponse"]]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsMaintenancePlansToMaintenancePlanResponse"] | None: ...
