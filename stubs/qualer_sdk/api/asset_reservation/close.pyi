from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.close_response_200 import CloseResponse200 as CloseResponse200
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    model_asset_id: Unset | int = ...,
    model_area_id: Unset | int = ...,
    model_product_id: Unset | int = ...,
    model_serial_number: Unset | str = ...,
    model_asset_tag: Unset | str = ...,
    model_reservation_id: Unset | int = ...,
) -> Response[CloseResponse200]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    model_asset_id: Unset | int = ...,
    model_area_id: Unset | int = ...,
    model_product_id: Unset | int = ...,
    model_serial_number: Unset | str = ...,
    model_asset_tag: Unset | str = ...,
    model_reservation_id: Unset | int = ...,
) -> CloseResponse200 | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    model_asset_id: Unset | int = ...,
    model_area_id: Unset | int = ...,
    model_product_id: Unset | int = ...,
    model_serial_number: Unset | str = ...,
    model_asset_tag: Unset | str = ...,
    model_reservation_id: Unset | int = ...,
) -> Response[CloseResponse200]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    model_asset_id: Unset | int = ...,
    model_area_id: Unset | int = ...,
    model_product_id: Unset | int = ...,
    model_serial_number: Unset | str = ...,
    model_asset_tag: Unset | str = ...,
    model_reservation_id: Unset | int = ...,
) -> CloseResponse200 | None: ...
