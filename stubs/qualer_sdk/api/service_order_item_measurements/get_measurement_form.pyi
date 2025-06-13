from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_measurements_to_update_measurement_form_response_model import (
    QualerApiModelsMeasurementsToUpdateMeasurementFormResponseModel as QualerApiModelsMeasurementsToUpdateMeasurementFormResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[
    Any | QualerApiModelsMeasurementsToUpdateMeasurementFormResponseModel
]: ...
def sync(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> Any | QualerApiModelsMeasurementsToUpdateMeasurementFormResponseModel | None: ...
async def asyncio_detailed(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> Response[
    Any | QualerApiModelsMeasurementsToUpdateMeasurementFormResponseModel
]: ...
async def asyncio(
    work_item_id: int, *, client: AuthenticatedClient | Client
) -> Any | QualerApiModelsMeasurementsToUpdateMeasurementFormResponseModel | None: ...
