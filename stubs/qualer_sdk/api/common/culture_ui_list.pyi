from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_common_to_culture_list_response_model import (
    QualerApiModelsCommonToCultureListResponseModel as QualerApiModelsCommonToCultureListResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsCommonToCultureListResponseModel]: ...
def sync(
    *, client: AuthenticatedClient | Client
) -> QualerApiModelsCommonToCultureListResponseModel | None: ...
async def asyncio_detailed(
    *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsCommonToCultureListResponseModel]: ...
async def asyncio(
    *, client: AuthenticatedClient | Client
) -> QualerApiModelsCommonToCultureListResponseModel | None: ...
