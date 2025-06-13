from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_measurements_from_update_measurement_form_model import (
    QualerApiModelsMeasurementsFromUpdateMeasurementFormModel as QualerApiModelsMeasurementsFromUpdateMeasurementFormModel,
)
from ...models.update_measurement_form_response_200 import (
    UpdateMeasurementFormResponse200 as UpdateMeasurementFormResponse200,
)
from ...types import Response as Response

def sync_detailed(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsMeasurementsFromUpdateMeasurementFormModel,
) -> Response[Any | UpdateMeasurementFormResponse200]: ...
def sync(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsMeasurementsFromUpdateMeasurementFormModel,
) -> Any | UpdateMeasurementFormResponse200 | None: ...
async def asyncio_detailed(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsMeasurementsFromUpdateMeasurementFormModel,
) -> Response[Any | UpdateMeasurementFormResponse200]: ...
async def asyncio(
    work_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsMeasurementsFromUpdateMeasurementFormModel,
) -> Any | UpdateMeasurementFormResponse200 | None: ...
