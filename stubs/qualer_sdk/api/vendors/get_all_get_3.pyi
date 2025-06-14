import datetime

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_vendors_to_vendor_company_response_model import (
    QualerApiModelsVendorsToVendorCompanyResponseModel as QualerApiModelsVendorsToVendorCompanyResponseModel,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    model_account_number_text: Unset | str = ...,
    model_company_name: Unset | str = ...,
    model_take: Unset | int = ...,
    model_modified_after: Unset | datetime.datetime = ...,
) -> Response[list["QualerApiModelsVendorsToVendorCompanyResponseModel"]]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    model_account_number_text: Unset | str = ...,
    model_company_name: Unset | str = ...,
    model_take: Unset | int = ...,
    model_modified_after: Unset | datetime.datetime = ...,
) -> list["QualerApiModelsVendorsToVendorCompanyResponseModel"] | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    model_account_number_text: Unset | str = ...,
    model_company_name: Unset | str = ...,
    model_take: Unset | int = ...,
    model_modified_after: Unset | datetime.datetime = ...,
) -> Response[list["QualerApiModelsVendorsToVendorCompanyResponseModel"]]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    model_account_number_text: Unset | str = ...,
    model_company_name: Unset | str = ...,
    model_take: Unset | int = ...,
    model_modified_after: Unset | datetime.datetime = ...,
) -> list["QualerApiModelsVendorsToVendorCompanyResponseModel"] | None: ...
