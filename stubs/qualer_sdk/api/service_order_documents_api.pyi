from _typeshed import Incomplete
from datetime import datetime
from pydantic import (
    Field as Field,
    StrictBool as StrictBool,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
    validate_arguments,
)
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import (
    ApiTypeError as ApiTypeError,
    ApiValueError as ApiValueError,
)
from qualer_sdk.models.qualer_api_models_service_order_documents_to_company_order_controlled_document_response import (
    QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse as QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse,
)
from typing_extensions import Annotated

class ServiceOrderDocumentsApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def get_document(self, guid: Annotated[StrictStr, None], **kwargs) -> object: ...
    @validate_arguments
    def get_document_with_http_info(
        self, guid: Annotated[StrictStr, None], **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_document_get_wd(
        self, guid: Annotated[StrictStr, None], **kwargs
    ) -> object: ...
    @validate_arguments
    def get_document_get_wd_with_http_info(
        self, guid: Annotated[StrictStr, None], **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_document_list(
        self,
        var_from: Annotated[datetime, None],
        to: Annotated[datetime, None],
        report_type: Annotated[StrictStr | None, None] = None,
        service_order_id: Annotated[StrictInt | None, None] = None,
        **kwargs,
    ) -> list[
        QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse
    ]: ...
    @validate_arguments
    def get_document_list_with_http_info(
        self,
        var_from: Annotated[datetime, None],
        to: Annotated[datetime, None],
        report_type: Annotated[StrictStr | None, None] = None,
        service_order_id: Annotated[StrictInt | None, None] = None,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def get_documents(
        self,
        service_order_id: StrictInt,
        model_file_name: StrictStr | None = None,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def get_documents_with_http_info(
        self,
        service_order_id: StrictInt,
        model_file_name: StrictStr | None = None,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def get_documents_list(
        self,
        service_order_id: StrictInt,
        model_report_type: StrictStr | None = None,
        **kwargs,
    ) -> list[
        QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse
    ]: ...
    @validate_arguments
    def get_documents_list_with_http_info(
        self,
        service_order_id: StrictInt,
        model_report_type: StrictStr | None = None,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def upload_documents_post2(
        self,
        service_order_id: StrictInt,
        model_report_type: StrictStr | None = None,
        model_is_private: StrictBool | None = None,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def upload_documents_post2_with_http_info(
        self,
        service_order_id: StrictInt,
        model_report_type: StrictStr | None = None,
        model_is_private: StrictBool | None = None,
        **kwargs,
    ) -> ApiResponse: ...
