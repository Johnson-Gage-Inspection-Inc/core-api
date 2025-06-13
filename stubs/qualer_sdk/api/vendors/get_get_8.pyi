from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_vendors_to_vendor_company_response_model import (
    QualerApiModelsVendorsToVendorCompanyResponseModel as QualerApiModelsVendorsToVendorCompanyResponseModel,
)
from ...types import Response as Response

def sync_detailed(
    vendor_company_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsVendorsToVendorCompanyResponseModel]: ...
def sync(
    vendor_company_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsVendorsToVendorCompanyResponseModel | None: ...
async def asyncio_detailed(
    vendor_company_id: int, *, client: AuthenticatedClient | Client
) -> Response[QualerApiModelsVendorsToVendorCompanyResponseModel]: ...
async def asyncio(
    vendor_company_id: int, *, client: AuthenticatedClient | Client
) -> QualerApiModelsVendorsToVendorCompanyResponseModel | None: ...
