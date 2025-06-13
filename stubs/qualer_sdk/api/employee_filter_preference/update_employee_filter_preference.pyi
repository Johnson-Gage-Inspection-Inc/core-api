from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_from_update_filter_preference_model import (
    QualerApiModelsAssetFromUpdateFilterPreferenceModel as QualerApiModelsAssetFromUpdateFilterPreferenceModel,
)
from ...models.update_employee_filter_preference_response_200 import (
    UpdateEmployeeFilterPreferenceResponse200 as UpdateEmployeeFilterPreferenceResponse200,
)
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateFilterPreferenceModel,
) -> Response[UpdateEmployeeFilterPreferenceResponse200]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateFilterPreferenceModel,
) -> UpdateEmployeeFilterPreferenceResponse200 | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateFilterPreferenceModel,
) -> Response[UpdateEmployeeFilterPreferenceResponse200]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetFromUpdateFilterPreferenceModel,
) -> UpdateEmployeeFilterPreferenceResponse200 | None: ...
