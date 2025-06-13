from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_order_item_parts_to_order_item_part_response_model import (
    QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel as QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[
    list["QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel"]
]: ...
def sync(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> (
    list["QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel"] | None
): ...
async def asyncio_detailed(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[
    list["QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel"]
]: ...
async def asyncio(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> (
    list["QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel"] | None
): ...
