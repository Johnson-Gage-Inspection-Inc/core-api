from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_client_attributes_from_client_attribute_model import (
    QualerApiModelsClientAttributesFromClientAttributeModel as QualerApiModelsClientAttributesFromClientAttributeModel,
)
from ...models.upsert_client_attribute_response_200 import (
    UpsertClientAttributeResponse200 as UpsertClientAttributeResponse200,
)
from ...types import Response as Response

def sync_detailed(
    client_company_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientAttributesFromClientAttributeModel,
) -> Response[UpsertClientAttributeResponse200]: ...
def sync(
    client_company_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientAttributesFromClientAttributeModel,
) -> UpsertClientAttributeResponse200 | None: ...
async def asyncio_detailed(
    client_company_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientAttributesFromClientAttributeModel,
) -> Response[UpsertClientAttributeResponse200]: ...
async def asyncio(
    client_company_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsClientAttributesFromClientAttributeModel,
) -> UpsertClientAttributeResponse200 | None: ...
