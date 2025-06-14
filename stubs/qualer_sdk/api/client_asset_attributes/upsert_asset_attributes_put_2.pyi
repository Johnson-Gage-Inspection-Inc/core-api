from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_common_from_attribute_model import (
    QualerApiModelsCommonFromAttributeModel as QualerApiModelsCommonFromAttributeModel,
)
from ...models.upsert_asset_attributes_put_2_response_200 import (
    UpsertAssetAttributesPut2Response200 as UpsertAssetAttributesPut2Response200,
)
from ...types import Response as Response

def sync_detailed(
    asset_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerApiModelsCommonFromAttributeModel"],
) -> Response[UpsertAssetAttributesPut2Response200]: ...
def sync(
    asset_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerApiModelsCommonFromAttributeModel"],
) -> UpsertAssetAttributesPut2Response200 | None: ...
async def asyncio_detailed(
    asset_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerApiModelsCommonFromAttributeModel"],
) -> Response[UpsertAssetAttributesPut2Response200]: ...
async def asyncio(
    asset_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerApiModelsCommonFromAttributeModel"],
) -> UpsertAssetAttributesPut2Response200 | None: ...
