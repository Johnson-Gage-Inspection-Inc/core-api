from _typeshed import Incomplete
from datetime import datetime
from pydantic import Field as Field, StrictInt as StrictInt, StrictStr as StrictStr, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from qualer_sdk.models.qualer_api_models_clients_from_sponsored_client_create_model import QualerApiModelsClientsFromSponsoredClientCreateModel as QualerApiModelsClientsFromSponsoredClientCreateModel
from qualer_sdk.models.qualer_api_models_clients_from_sponsored_client_edit_model import QualerApiModelsClientsFromSponsoredClientEditModel as QualerApiModelsClientsFromSponsoredClientEditModel
from qualer_sdk.models.qualer_api_models_clients_to_client_company_response_model import QualerApiModelsClientsToClientCompanyResponseModel as QualerApiModelsClientsToClientCompanyResponseModel
from qualer_sdk.models.qualer_api_models_clients_to_created_client_company_response import QualerApiModelsClientsToCreatedClientCompanyResponse as QualerApiModelsClientsToCreatedClientCompanyResponse
from typing_extensions import Annotated

class ClientsApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def create(self, model: Annotated[QualerApiModelsClientsFromSponsoredClientCreateModel, None], **kwargs) -> QualerApiModelsClientsToCreatedClientCompanyResponse: ...
    @validate_arguments
    def create_with_http_info(self, model: Annotated[QualerApiModelsClientsFromSponsoredClientCreateModel, None], **kwargs) -> ApiResponse: ...
    @validate_arguments
    def get_all_get2(self, model_legacy_id: StrictStr | None = None, model_account_number_text: StrictStr | None = None, model_company_name: StrictStr | None = None, model_take: StrictInt | None = None, model_modified_after: datetime | None = None, **kwargs) -> list[QualerApiModelsClientsToClientCompanyResponseModel]: ...
    @validate_arguments
    def get_all_get2_with_http_info(self, model_legacy_id: StrictStr | None = None, model_account_number_text: StrictStr | None = None, model_company_name: StrictStr | None = None, model_take: StrictInt | None = None, model_modified_after: datetime | None = None, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def get_get3(self, client_company_id: StrictInt, **kwargs) -> QualerApiModelsClientsToClientCompanyResponseModel: ...
    @validate_arguments
    def get_get3_with_http_info(self, client_company_id: StrictInt, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def update(self, model: Annotated[QualerApiModelsClientsFromSponsoredClientEditModel, None], **kwargs) -> object: ...
    @validate_arguments
    def update_with_http_info(self, model: Annotated[QualerApiModelsClientsFromSponsoredClientEditModel, None], **kwargs) -> ApiResponse: ...
