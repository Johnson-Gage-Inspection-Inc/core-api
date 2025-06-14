import datetime

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_reservation_to_asset_reservation_response import (
    QualerApiModelsAssetReservationToAssetReservationResponse as QualerApiModelsAssetReservationToAssetReservationResponse,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    model_from: Unset | datetime.datetime = ...,
    model_to: Unset | datetime.datetime = ...,
    model_asset_id: Unset | int = ...,
    model_area_id: Unset | int = ...,
    model_product_id: Unset | int = ...,
    model_serial_number: Unset | str = ...,
    model_asset_tag: Unset | str = ...,
    model_reservation_id: Unset | int = ...,
) -> Response[list["QualerApiModelsAssetReservationToAssetReservationResponse"]]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    model_from: Unset | datetime.datetime = ...,
    model_to: Unset | datetime.datetime = ...,
    model_asset_id: Unset | int = ...,
    model_area_id: Unset | int = ...,
    model_product_id: Unset | int = ...,
    model_serial_number: Unset | str = ...,
    model_asset_tag: Unset | str = ...,
    model_reservation_id: Unset | int = ...,
) -> list["QualerApiModelsAssetReservationToAssetReservationResponse"] | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    model_from: Unset | datetime.datetime = ...,
    model_to: Unset | datetime.datetime = ...,
    model_asset_id: Unset | int = ...,
    model_area_id: Unset | int = ...,
    model_product_id: Unset | int = ...,
    model_serial_number: Unset | str = ...,
    model_asset_tag: Unset | str = ...,
    model_reservation_id: Unset | int = ...,
) -> Response[list["QualerApiModelsAssetReservationToAssetReservationResponse"]]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    model_from: Unset | datetime.datetime = ...,
    model_to: Unset | datetime.datetime = ...,
    model_asset_id: Unset | int = ...,
    model_area_id: Unset | int = ...,
    model_product_id: Unset | int = ...,
    model_serial_number: Unset | str = ...,
    model_asset_tag: Unset | str = ...,
    model_reservation_id: Unset | int = ...,
) -> list["QualerApiModelsAssetReservationToAssetReservationResponse"] | None: ...
