from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_to_asset_manage_response_model import (
    QualerApiModelsAssetToAssetManageResponseModel as QualerApiModelsAssetToAssetManageResponseModel,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    model_filter_type: Unset | str = ...,
    model_search_string: Unset | str = ...,
    model_page: Unset | int = ...,
    model_page_size: Unset | int = ...,
) -> Response[list["QualerApiModelsAssetToAssetManageResponseModel"]]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    model_filter_type: Unset | str = ...,
    model_search_string: Unset | str = ...,
    model_page: Unset | int = ...,
    model_page_size: Unset | int = ...,
) -> list["QualerApiModelsAssetToAssetManageResponseModel"] | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    model_filter_type: Unset | str = ...,
    model_search_string: Unset | str = ...,
    model_page: Unset | int = ...,
    model_page_size: Unset | int = ...,
) -> Response[list["QualerApiModelsAssetToAssetManageResponseModel"]]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    model_filter_type: Unset | str = ...,
    model_search_string: Unset | str = ...,
    model_page: Unset | int = ...,
    model_page_size: Unset | int = ...,
) -> list["QualerApiModelsAssetToAssetManageResponseModel"] | None: ...
