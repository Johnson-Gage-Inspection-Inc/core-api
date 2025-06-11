from _typeshed import Incomplete
from pydantic import StrictInt as StrictInt, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import (
    ApiTypeError as ApiTypeError,
    ApiValueError as ApiValueError,
)
from qualer_sdk.models.qualer_api_models_service_orders_from_service_order_task_create_model import (
    QualerApiModelsServiceOrdersFromServiceOrderTaskCreateModel as QualerApiModelsServiceOrdersFromServiceOrderTaskCreateModel,
)
from qualer_sdk.models.qualer_api_models_service_orders_from_service_order_task_update_model import (
    QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel as QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel,
)
from qualer_sdk.models.qualer_api_models_service_orders_to_service_order_task_response import (
    QualerApiModelsServiceOrdersToServiceOrderTaskResponse as QualerApiModelsServiceOrdersToServiceOrderTaskResponse,
)

class ServiceOrderTasksApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def create_work_order_task(
        self,
        service_order_id: StrictInt,
        model: QualerApiModelsServiceOrdersFromServiceOrderTaskCreateModel,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def create_work_order_task_with_http_info(
        self,
        service_order_id: StrictInt,
        model: QualerApiModelsServiceOrdersFromServiceOrderTaskCreateModel,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def delete_work_order_task_delete2(
        self, service_order_id: StrictInt, service_order_task_id: StrictInt, **kwargs
    ) -> object: ...
    @validate_arguments
    def delete_work_order_task_delete2_with_http_info(
        self, service_order_id: StrictInt, service_order_task_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_work_order_tasks(
        self, service_order_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsServiceOrdersToServiceOrderTaskResponse]: ...
    @validate_arguments
    def get_work_order_tasks_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def update_work_order_task(
        self,
        service_order_id: StrictInt,
        model: QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def update_work_order_task_with_http_info(
        self,
        service_order_id: StrictInt,
        model: QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel,
        **kwargs,
    ) -> ApiResponse: ...
