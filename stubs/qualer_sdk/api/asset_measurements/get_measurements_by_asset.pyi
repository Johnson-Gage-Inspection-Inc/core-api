import datetime

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_measurements_to_measurement_record_response_model import (
    QualerApiModelsMeasurementsToMeasurementRecordResponseModel as QualerApiModelsMeasurementsToMeasurementRecordResponseModel,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    asset_id: int,
    *,
    client: AuthenticatedClient | Client,
    from_: Unset | datetime.datetime = ...,
    to: Unset | datetime.datetime = ...,
) -> Response[list["QualerApiModelsMeasurementsToMeasurementRecordResponseModel"]]: ...
def sync(
    asset_id: int,
    *,
    client: AuthenticatedClient | Client,
    from_: Unset | datetime.datetime = ...,
    to: Unset | datetime.datetime = ...,
) -> list["QualerApiModelsMeasurementsToMeasurementRecordResponseModel"] | None: ...
async def asyncio_detailed(
    asset_id: int,
    *,
    client: AuthenticatedClient | Client,
    from_: Unset | datetime.datetime = ...,
    to: Unset | datetime.datetime = ...,
) -> Response[list["QualerApiModelsMeasurementsToMeasurementRecordResponseModel"]]: ...
async def asyncio(
    asset_id: int,
    *,
    client: AuthenticatedClient | Client,
    from_: Unset | datetime.datetime = ...,
    to: Unset | datetime.datetime = ...,
) -> list["QualerApiModelsMeasurementsToMeasurementRecordResponseModel"] | None: ...
