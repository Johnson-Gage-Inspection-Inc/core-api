from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_to_client_asset_manager_response_model import (
    QualerApiModelsAssetToClientAssetManagerResponseModel as QualerApiModelsAssetToClientAssetManagerResponseModel,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    client_company_id: int,
    *,
    client: AuthenticatedClient | Client,
    query_filter_type: Unset | str = ...,
    query_search_string: Unset | str = ...,
    query_page: Unset | int = ...,
    query_page_size: Unset | int = ...,
) -> Response[list["QualerApiModelsAssetToClientAssetManagerResponseModel"]]: ...
def sync(
    client_company_id: int,
    *,
    client: AuthenticatedClient | Client,
    query_filter_type: Unset | str = ...,
    query_search_string: Unset | str = ...,
    query_page: Unset | int = ...,
    query_page_size: Unset | int = ...,
) -> list["QualerApiModelsAssetToClientAssetManagerResponseModel"] | None: ...
async def asyncio_detailed(
    client_company_id: int,
    *,
    client: AuthenticatedClient | Client,
    query_filter_type: Unset | str = ...,
    query_search_string: Unset | str = ...,
    query_page: Unset | int = ...,
    query_page_size: Unset | int = ...,
) -> Response[list["QualerApiModelsAssetToClientAssetManagerResponseModel"]]: ...
async def asyncio(
    client_company_id: int,
    *,
    client: AuthenticatedClient | Client,
    query_filter_type: Unset | str = ...,
    query_search_string: Unset | str = ...,
    query_page: Unset | int = ...,
    query_page_size: Unset | int = ...,
) -> list["QualerApiModelsAssetToClientAssetManagerResponseModel"] | None: ...
