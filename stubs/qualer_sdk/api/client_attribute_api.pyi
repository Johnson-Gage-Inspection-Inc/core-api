from _typeshed import Incomplete
from pydantic import StrictInt as StrictInt, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import (
    ApiTypeError as ApiTypeError,
    ApiValueError as ApiValueError,
)
from qualer_sdk.models.qualer_api_models_client_attributes_from_client_attribute_model import (
    QualerApiModelsClientAttributesFromClientAttributeModel as QualerApiModelsClientAttributesFromClientAttributeModel,
)

class ClientAttributeApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def get_client_attributes(
        self, client_company_id: StrictInt, **kwargs
    ) -> object: ...
    @validate_arguments
    def get_client_attributes_with_http_info(
        self, client_company_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def upsert_client_attribute(
        self,
        client_company_id: StrictInt,
        model: QualerApiModelsClientAttributesFromClientAttributeModel,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def upsert_client_attribute_with_http_info(
        self,
        client_company_id: StrictInt,
        model: QualerApiModelsClientAttributesFromClientAttributeModel,
        **kwargs,
    ) -> ApiResponse: ...
