from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_vendors_from_sponsored_vendor_edit_model import (
    QualerApiModelsVendorsFromSponsoredVendorEditModel as QualerApiModelsVendorsFromSponsoredVendorEditModel,
)
from ...models.update_put_4_response_200 import (
    UpdatePut4Response200 as UpdatePut4Response200,
)
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsVendorsFromSponsoredVendorEditModel,
) -> Response[Any | UpdatePut4Response200]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsVendorsFromSponsoredVendorEditModel,
) -> Any | UpdatePut4Response200 | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsVendorsFromSponsoredVendorEditModel,
) -> Response[Any | UpdatePut4Response200]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsVendorsFromSponsoredVendorEditModel,
) -> Any | UpdatePut4Response200 | None: ...
