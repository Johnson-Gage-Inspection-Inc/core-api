from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.get_get_4_element_page import GetGet4ElementPage as GetGet4ElementPage
from ...models.qualer_api_models_asset_to_employee_preference_response_model import (
    QualerApiModelsAssetToEmployeePreferenceResponseModel as QualerApiModelsAssetToEmployeePreferenceResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    element_page: GetGet4ElementPage, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsAssetToEmployeePreferenceResponseModel"]]: ...
def sync(
    element_page: GetGet4ElementPage, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsAssetToEmployeePreferenceResponseModel"] | None: ...
async def asyncio_detailed(
    element_page: GetGet4ElementPage, *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsAssetToEmployeePreferenceResponseModel"]]: ...
async def asyncio(
    element_page: GetGet4ElementPage, *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsAssetToEmployeePreferenceResponseModel"] | None: ...
