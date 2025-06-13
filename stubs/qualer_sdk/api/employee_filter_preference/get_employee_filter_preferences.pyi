from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_to_employee_filter_preference_response_model import (
    QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel as QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel"]]: ...
def sync(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel"] | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[list["QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel"]]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client
) -> list["QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel"] | None: ...
