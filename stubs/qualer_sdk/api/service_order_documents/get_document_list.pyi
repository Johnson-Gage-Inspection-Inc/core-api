import datetime
from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_order_documents_to_company_order_controlled_document_response import (
    QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse as QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse,
)
from ...types import UNSET as UNSET
from ...types import Response as Response
from ...types import Unset as Unset

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime,
    to: datetime.datetime,
    report_type: Unset | str = ...,
    service_order_id: Unset | int = ...,
) -> Response[
    Any
    | list[
        "QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse"
    ]
]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime,
    to: datetime.datetime,
    report_type: Unset | str = ...,
    service_order_id: Unset | int = ...,
) -> (
    Any
    | list[
        "QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse"
    ]
    | None
): ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime,
    to: datetime.datetime,
    report_type: Unset | str = ...,
    service_order_id: Unset | int = ...,
) -> Response[
    Any
    | list[
        "QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse"
    ]
]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime,
    to: datetime.datetime,
    report_type: Unset | str = ...,
    service_order_id: Unset | int = ...,
) -> (
    Any
    | list[
        "QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse"
    ]
    | None
): ...
