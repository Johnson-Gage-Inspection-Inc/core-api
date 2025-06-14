from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_common_to_setting_response_model import (
    QualerApiModelsCommonToSettingResponseModel as QualerApiModelsCommonToSettingResponseModel,
)
from ...types import UNSET as UNSET
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client, setting_key: str
) -> Response[QualerApiModelsCommonToSettingResponseModel]: ...
def sync(
    *, client: AuthenticatedClient | Client, setting_key: str
) -> QualerApiModelsCommonToSettingResponseModel | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client, setting_key: str
) -> Response[QualerApiModelsCommonToSettingResponseModel]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client, setting_key: str
) -> QualerApiModelsCommonToSettingResponseModel | None: ...
