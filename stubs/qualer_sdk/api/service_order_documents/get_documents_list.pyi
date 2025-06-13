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
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_report_type: Unset | str = ...,
) -> Response[
    Any
    | list[
        "QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse"
    ]
]: ...
def sync(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_report_type: Unset | str = ...,
) -> (
    Any
    | list[
        "QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse"
    ]
    | None
): ...
async def asyncio_detailed(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_report_type: Unset | str = ...,
) -> Response[
    Any
    | list[
        "QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse"
    ]
]: ...
async def asyncio(
    service_order_id: int,
    *,
    client: AuthenticatedClient | Client,
    model_report_type: Unset | str = ...,
) -> (
    Any
    | list[
        "QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse"
    ]
    | None
): ...
