from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_vendors_from_sponsored_vendor_create_model import (
    QualerApiModelsVendorsFromSponsoredVendorCreateModel as QualerApiModelsVendorsFromSponsoredVendorCreateModel,
)
from ...models.qualer_api_models_vendors_to_created_vendor_company_response import (
    QualerApiModelsVendorsToCreatedVendorCompanyResponse as QualerApiModelsVendorsToCreatedVendorCompanyResponse,
)
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsVendorsFromSponsoredVendorCreateModel,
) -> Response[Any | QualerApiModelsVendorsToCreatedVendorCompanyResponse]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsVendorsFromSponsoredVendorCreateModel,
) -> Any | QualerApiModelsVendorsToCreatedVendorCompanyResponse | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsVendorsFromSponsoredVendorCreateModel,
) -> Response[Any | QualerApiModelsVendorsToCreatedVendorCompanyResponse]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsVendorsFromSponsoredVendorCreateModel,
) -> Any | QualerApiModelsVendorsToCreatedVendorCompanyResponse | None: ...
