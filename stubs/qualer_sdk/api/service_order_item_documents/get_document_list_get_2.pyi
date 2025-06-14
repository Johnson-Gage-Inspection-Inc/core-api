import datetime
from typing import Any

from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_service_order_documents_to_company_order_item_controlled_document_response import (
    QualerApiModelsServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse as QualerApiModelsServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse,
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
    service_order_item_id: Unset | int = ...,
) -> Response[
    Any
    | list[
        "QualerApiModelsServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse"
    ]
]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime,
    to: datetime.datetime,
    report_type: Unset | str = ...,
    service_order_item_id: Unset | int = ...,
) -> (
    Any
    | list[
        "QualerApiModelsServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse"
    ]
    | None
): ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime,
    to: datetime.datetime,
    report_type: Unset | str = ...,
    service_order_item_id: Unset | int = ...,
) -> Response[
    Any
    | list[
        "QualerApiModelsServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse"
    ]
]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime,
    to: datetime.datetime,
    report_type: Unset | str = ...,
    service_order_item_id: Unset | int = ...,
) -> (
    Any
    | list[
        "QualerApiModelsServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse"
    ]
    | None
): ...
