import datetime

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_clients_to_client_company_response_model import (
    QualerApiModelsClientsToClientCompanyResponseModel as QualerApiModelsClientsToClientCompanyResponseModel,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    model_legacy_id: Unset | str = ...,
    model_account_number_text: Unset | str = ...,
    model_company_name: Unset | str = ...,
    model_take: Unset | int = ...,
    model_modified_after: Unset | datetime.datetime = ...,
) -> Response[list["QualerApiModelsClientsToClientCompanyResponseModel"]]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    model_legacy_id: Unset | str = ...,
    model_account_number_text: Unset | str = ...,
    model_company_name: Unset | str = ...,
    model_take: Unset | int = ...,
    model_modified_after: Unset | datetime.datetime = ...,
) -> list["QualerApiModelsClientsToClientCompanyResponseModel"] | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    model_legacy_id: Unset | str = ...,
    model_account_number_text: Unset | str = ...,
    model_company_name: Unset | str = ...,
    model_take: Unset | int = ...,
    model_modified_after: Unset | datetime.datetime = ...,
) -> Response[list["QualerApiModelsClientsToClientCompanyResponseModel"]]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    model_legacy_id: Unset | str = ...,
    model_account_number_text: Unset | str = ...,
    model_company_name: Unset | str = ...,
    model_take: Unset | int = ...,
    model_modified_after: Unset | datetime.datetime = ...,
) -> list["QualerApiModelsClientsToClientCompanyResponseModel"] | None: ...
