from _typeshed import Incomplete
from pydantic import Field as Field, StrictInt as StrictInt, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from qualer_sdk.models.qualer_api_models_site_from_site_create_model import QualerApiModelsSiteFromSiteCreateModel as QualerApiModelsSiteFromSiteCreateModel
from qualer_sdk.models.qualer_api_models_site_from_site_update_model import QualerApiModelsSiteFromSiteUpdateModel as QualerApiModelsSiteFromSiteUpdateModel
from qualer_sdk.models.qualer_api_models_site_to_client_site_response import QualerApiModelsSiteToClientSiteResponse as QualerApiModelsSiteToClientSiteResponse
from typing_extensions import Annotated

class ClientSiteApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def create_client_site(self, client_company_id: Annotated[StrictInt, None], model: Annotated[QualerApiModelsSiteFromSiteCreateModel, None], **kwargs) -> object: ...
    @validate_arguments
    def create_client_site_with_http_info(self, client_company_id: Annotated[StrictInt, None], model: Annotated[QualerApiModelsSiteFromSiteCreateModel, None], **kwargs) -> ApiResponse: ...
    @validate_arguments
    def get_client_sites(self, client_company_id: StrictInt, **kwargs) -> list[QualerApiModelsSiteToClientSiteResponse]: ...
    @validate_arguments
    def get_client_sites_with_http_info(self, client_company_id: StrictInt, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def update_client_site(self, client_company_id: Annotated[StrictInt, None], model: Annotated[QualerApiModelsSiteFromSiteUpdateModel, None], **kwargs) -> object: ...
    @validate_arguments
    def update_client_site_with_http_info(self, client_company_id: Annotated[StrictInt, None], model: Annotated[QualerApiModelsSiteFromSiteUpdateModel, None], **kwargs) -> ApiResponse: ...
