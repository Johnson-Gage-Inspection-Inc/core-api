from _typeshed import Incomplete
from pydantic import StrictInt as StrictInt, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from qualer_sdk.models.qualer_api_models_service_order_item_parts_to_order_item_part_response_model import QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel as QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel

class ServiceOrderItemPartsApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def get_work_item_parts(self, work_item_id: StrictInt, **kwargs) -> list[QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel]: ...
    @validate_arguments
    def get_work_item_parts_with_http_info(self, work_item_id: StrictInt, **kwargs) -> ApiResponse: ...
