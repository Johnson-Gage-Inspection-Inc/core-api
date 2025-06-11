from _typeshed import Incomplete
from pydantic import (
    Field as Field,
    StrictInt as StrictInt,
    conlist as conlist,
    validate_arguments,
)
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import (
    ApiTypeError as ApiTypeError,
    ApiValueError as ApiValueError,
)
from qualer_sdk.models.qualer_api_models_service_orders_to_service_order_task_response import (
    QualerApiModelsServiceOrdersToServiceOrderTaskResponse as QualerApiModelsServiceOrdersToServiceOrderTaskResponse,
)
from qualer_sdk.models.qualer_web_mvc_areas_api_models_service_prices_from_service_price_bulk_edit_model import (
    QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel as QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel,
)
from typing_extensions import Annotated

class ServicePricingApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def get_get7(
        self,
        service_pricing_id: StrictInt,
        service_group_id: Annotated[StrictInt | None, None] = None,
        **kwargs,
    ) -> list[QualerApiModelsServiceOrdersToServiceOrderTaskResponse]: ...
    @validate_arguments
    def get_get7_with_http_info(
        self,
        service_pricing_id: StrictInt,
        service_group_id: Annotated[StrictInt | None, None] = None,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def update_put3(
        self, models: None, **kwargs
    ) -> list[QualerApiModelsServiceOrdersToServiceOrderTaskResponse]: ...
    @validate_arguments
    def update_put3_with_http_info(self, models: None, **kwargs) -> ApiResponse: ...
