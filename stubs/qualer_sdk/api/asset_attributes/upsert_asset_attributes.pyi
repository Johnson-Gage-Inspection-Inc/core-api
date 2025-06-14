from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_common_from_attribute_model import (
    QualerApiModelsCommonFromAttributeModel as QualerApiModelsCommonFromAttributeModel,
)
from ...models.upsert_asset_attributes_response_200 import (
    UpsertAssetAttributesResponse200 as UpsertAssetAttributesResponse200,
)
from ...types import Response as Response

def sync_detailed(
    asset_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerApiModelsCommonFromAttributeModel"],
) -> Response[UpsertAssetAttributesResponse200]: ...
def sync(
    asset_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerApiModelsCommonFromAttributeModel"],
) -> UpsertAssetAttributesResponse200 | None: ...
async def asyncio_detailed(
    asset_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerApiModelsCommonFromAttributeModel"],
) -> Response[UpsertAssetAttributesResponse200]: ...
async def asyncio(
    asset_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: list["QualerApiModelsCommonFromAttributeModel"],
) -> UpsertAssetAttributesResponse200 | None: ...
