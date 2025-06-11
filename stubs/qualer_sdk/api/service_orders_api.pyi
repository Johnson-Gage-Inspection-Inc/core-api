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
from qualer_sdk.models.qualer_api_models_service_orders_from_change_service_order_status_model import (
    QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel as QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel,
)
from qualer_sdk.models.qualer_api_models_service_orders_from_charge_update_model import (
    QualerApiModelsServiceOrdersFromChargeUpdateModel as QualerApiModelsServiceOrdersFromChargeUpdateModel,
)
from qualer_sdk.models.qualer_api_models_service_orders_from_create_order_model import (
    QualerApiModelsServiceOrdersFromCreateOrderModel as QualerApiModelsServiceOrdersFromCreateOrderModel,
)
from qualer_sdk.models.qualer_api_models_service_orders_to_client_order_response_model import (
    QualerApiModelsServiceOrdersToClientOrderResponseModel as QualerApiModelsServiceOrdersToClientOrderResponseModel,
)
from qualer_sdk.models.qualer_api_models_service_orders_to_order_assignment_response_model import (
    QualerApiModelsServiceOrdersToOrderAssignmentResponseModel as QualerApiModelsServiceOrdersToOrderAssignmentResponseModel,
)
from qualer_sdk.models.qualer_api_models_service_orders_to_provider_service_order_response_model import (
    QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel as QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel,
)
from qualer_sdk.models.qualer_web_mvc_areas_api_models_service_orders_to_charge_response_model import (
    QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel as QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel,
)
from typing_extensions import Annotated

class ServiceOrdersApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def change_order_status(
        self,
        service_order_id: StrictInt,
        model: QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def change_order_status_with_http_info(
        self,
        service_order_id: StrictInt,
        model: QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def create_async(
        self,
        model: Annotated[QualerApiModelsServiceOrdersFromCreateOrderModel, None],
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def create_async_with_http_info(
        self,
        model: Annotated[QualerApiModelsServiceOrdersFromCreateOrderModel, None],
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def create_order_by_schedule(
        self, service_schedule_id: StrictInt, **kwargs
    ) -> object: ...
    @validate_arguments
    def create_order_by_schedule_with_http_info(
        self, service_schedule_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_assignments(
        self, service_order_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsServiceOrdersToOrderAssignmentResponseModel]: ...
    @validate_arguments
    def get_assignments_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_charges(
        self, service_order_id: StrictInt, **kwargs
    ) -> QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel: ...
    @validate_arguments
    def get_charges_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_order_status(self, service_order_id: StrictInt, **kwargs) -> object: ...
    @validate_arguments
    def get_order_status_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_work_order(
        self, service_order_id: StrictInt, **kwargs
    ) -> QualerApiModelsServiceOrdersToClientOrderResponseModel: ...
    @validate_arguments
    def get_work_order_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_work_orders(
        self,
        status: Annotated[StrictStr | None, None] = None,
        company_id: Annotated[StrictInt | None, None] = None,
        var_from: Annotated[datetime | None, None] = None,
        to: Annotated[datetime | None, None] = None,
        modified_after: Annotated[datetime | None, None] = None,
        work_order_number: Annotated[StrictStr | None, None] = None,
        assigned_employees: Annotated[StrictStr | None, None] = None,
        **kwargs,
    ) -> list[QualerApiModelsServiceOrdersToClientOrderResponseModel]: ...
    @validate_arguments
    def get_work_orders_with_http_info(
        self,
        status: Annotated[StrictStr | None, None] = None,
        company_id: Annotated[StrictInt | None, None] = None,
        var_from: Annotated[datetime | None, None] = None,
        to: Annotated[datetime | None, None] = None,
        modified_after: Annotated[datetime | None, None] = None,
        work_order_number: Annotated[StrictStr | None, None] = None,
        assigned_employees: Annotated[StrictStr | None, None] = None,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def get_work_orders_employee(
        self, employee_id: StrictInt, is_internal: StrictBool | None = None, **kwargs
    ) -> list[QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel]: ...
    @validate_arguments
    def get_work_orders_employee_with_http_info(
        self, employee_id: StrictInt, is_internal: StrictBool | None = None, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def order_cancel(
        self,
        service_order_id: StrictInt,
        reason_text: Annotated[StrictStr | None, None] = None,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def order_cancel_with_http_info(
        self,
        service_order_id: StrictInt,
        reason_text: Annotated[StrictStr | None, None] = None,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def put_charges_put2(
        self,
        service_order_id: StrictInt,
        model: QualerApiModelsServiceOrdersFromChargeUpdateModel,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def put_charges_put2_with_http_info(
        self,
        service_order_id: StrictInt,
        model: QualerApiModelsServiceOrdersFromChargeUpdateModel,
        **kwargs,
    ) -> ApiResponse: ...
