from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.create_measurement_form_response_200 import (
    CreateMeasurementFormResponse200 as CreateMeasurementFormResponse200,
)
from ...models.qualer_api_models_measurements_from_create_measurement_form_model import (
    QualerApiModelsMeasurementsFromCreateMeasurementFormModel as QualerApiModelsMeasurementsFromCreateMeasurementFormModel,
)
from ...types import Response as Response

def sync_detailed(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsMeasurementsFromCreateMeasurementFormModel,
) -> Response[Any | CreateMeasurementFormResponse200]: ...
def sync(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsMeasurementsFromCreateMeasurementFormModel,
) -> Any | CreateMeasurementFormResponse200 | None: ...
async def asyncio_detailed(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsMeasurementsFromCreateMeasurementFormModel,
) -> Response[Any | CreateMeasurementFormResponse200]: ...
async def asyncio(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsMeasurementsFromCreateMeasurementFormModel,
) -> Any | CreateMeasurementFormResponse200 | None: ...
