from _typeshed import Incomplete
from pydantic import StrictStr as StrictStr, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from qualer_sdk.models.qualer_api_models_environment_from_environment_model import QualerApiModelsEnvironmentFromEnvironmentModel as QualerApiModelsEnvironmentFromEnvironmentModel
from qualer_sdk.models.qualer_api_models_environment_to_environment_model import QualerApiModelsEnvironmentToEnvironmentModel as QualerApiModelsEnvironmentToEnvironmentModel

class EnvironmentsApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def get_get5(self, id: StrictStr, **kwargs) -> list[QualerApiModelsEnvironmentToEnvironmentModel]: ...
    @validate_arguments
    def get_get5_with_http_info(self, id: StrictStr, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def post(self, id: StrictStr, model: QualerApiModelsEnvironmentFromEnvironmentModel, **kwargs) -> object: ...
    @validate_arguments
    def post_with_http_info(self, id: StrictStr, model: QualerApiModelsEnvironmentFromEnvironmentModel, **kwargs) -> ApiResponse: ...
