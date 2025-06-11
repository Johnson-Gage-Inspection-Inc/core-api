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
from qualer_sdk.models.qualer_api_models_service_order_documents_to_company_order_item_controlled_document_response import (
    QualerApiModelsServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse as QualerApiModelsServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse,
)
from typing_extensions import Annotated

class ServiceOrderItemDocumentsApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def get_document_list_get2(
        self,
        var_from: Annotated[datetime, None],
        to: Annotated[datetime, None],
        report_type: Annotated[StrictStr | None, None] = None,
        service_order_item_id: Annotated[StrictInt | None, None] = None,
        **kwargs,
    ) -> list[
        QualerApiModelsServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse
    ]: ...
    @validate_arguments
    def get_document_list_get2_with_http_info(
        self,
        var_from: Annotated[datetime, None],
        to: Annotated[datetime, None],
        report_type: Annotated[StrictStr | None, None] = None,
        service_order_item_id: Annotated[StrictInt | None, None] = None,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def get_documents_get2(
        self,
        service_order_item_id: Annotated[StrictInt, None],
        model_file_name: StrictStr | None = None,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def get_documents_get2_with_http_info(
        self,
        service_order_item_id: Annotated[StrictInt, None],
        model_file_name: StrictStr | None = None,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def get_documents_list_get2(
        self,
        service_order_item_id: StrictInt,
        model_report_type: StrictStr | None = None,
        **kwargs,
    ) -> list[
        QualerApiModelsServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse
    ]: ...
    @validate_arguments
    def get_documents_list_get2_with_http_info(
        self,
        service_order_item_id: StrictInt,
        model_report_type: StrictStr | None = None,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def upload_documents_post3(
        self,
        service_order_item_id: StrictInt,
        model_report_type: StrictStr | None = None,
        model_is_private: StrictBool | None = None,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def upload_documents_post3_with_http_info(
        self,
        service_order_item_id: StrictInt,
        model_report_type: StrictStr | None = None,
        model_is_private: StrictBool | None = None,
        **kwargs,
    ) -> ApiResponse: ...
