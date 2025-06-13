from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.add_auxiliary_tools_response_200 import (
    AddAuxiliaryToolsResponse200 as AddAuxiliaryToolsResponse200,
)
from ...models.qualer_api_models_measurements_from_create_measurement_tool_model import (
    QualerApiModelsMeasurementsFromCreateMeasurementToolModel as QualerApiModelsMeasurementsFromCreateMeasurementToolModel,
)
from ...types import Response as Response

def sync_detailed(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerApiModelsMeasurementsFromCreateMeasurementToolModel"],
) -> Response[AddAuxiliaryToolsResponse200]: ...
def sync(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerApiModelsMeasurementsFromCreateMeasurementToolModel"],
) -> AddAuxiliaryToolsResponse200 | None: ...
async def asyncio_detailed(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerApiModelsMeasurementsFromCreateMeasurementToolModel"],
) -> Response[AddAuxiliaryToolsResponse200]: ...
async def asyncio(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerApiModelsMeasurementsFromCreateMeasurementToolModel"],
) -> AddAuxiliaryToolsResponse200 | None: ...
