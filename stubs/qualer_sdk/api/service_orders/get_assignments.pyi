from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_orders_to_order_assignment_response_model import (
    QualerApiModelsServiceOrdersToOrderAssignmentResponseModel as QualerApiModelsServiceOrdersToOrderAssignmentResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsServiceOrdersToOrderAssignmentResponseModel"]]: ...
def sync(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsServiceOrdersToOrderAssignmentResponseModel"] | None: ...
async def asyncio_detailed(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsServiceOrdersToOrderAssignmentResponseModel"]]: ...
async def asyncio(
    service_order_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsServiceOrdersToOrderAssignmentResponseModel"] | None: ...
