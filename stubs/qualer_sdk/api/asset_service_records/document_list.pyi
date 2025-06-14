from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    asset_service_record_id_path: str,
    *,
    client: AuthenticatedClient | Client,
    asset_service_record_id_query: Unset | str = ...,
    model_asset_service_record_id: Unset | int = ...,
) -> Response[list[str]]: ...
def sync(
    asset_service_record_id_path: str,
    *,
    client: AuthenticatedClient | Client,
    asset_service_record_id_query: Unset | str = ...,
    model_asset_service_record_id: Unset | int = ...,
) -> list[str] | None: ...
async def asyncio_detailed(
    asset_service_record_id_path: str,
    *,
    client: AuthenticatedClient | Client,
    asset_service_record_id_query: Unset | str = ...,
    model_asset_service_record_id: Unset | int = ...,
) -> Response[list[str]]: ...
async def asyncio(
    asset_service_record_id_path: str,
    *,
    client: AuthenticatedClient | Client,
    asset_service_record_id_query: Unset | str = ...,
    model_asset_service_record_id: Unset | int = ...,
) -> list[str] | None: ...
