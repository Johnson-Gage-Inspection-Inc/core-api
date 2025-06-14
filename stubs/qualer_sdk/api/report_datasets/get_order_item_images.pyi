from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_report_datasets_to_order_item_image_response import (
    QualerApiModelsReportDatasetsToOrderItemImageResponse as QualerApiModelsReportDatasetsToOrderItemImageResponse,
)
from ...types import Response as Response

def sync_detailed(
    service_order_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReportDatasetsToOrderItemImageResponse"]]: ...
def sync(
    service_order_item_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReportDatasetsToOrderItemImageResponse"] | None: ...
async def asyncio_detailed(
    service_order_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsReportDatasetsToOrderItemImageResponse"]]: ...
async def asyncio(
    service_order_item_id: int, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsReportDatasetsToOrderItemImageResponse"] | None: ...
