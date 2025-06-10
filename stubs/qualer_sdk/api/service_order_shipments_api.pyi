from _typeshed import Incomplete
from pydantic import StrictInt as StrictInt, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from qualer_sdk.models.qualer_api_models_service_orders_from_append_tracking_number_model import QualerApiModelsServiceOrdersFromAppendTrackingNumberModel as QualerApiModelsServiceOrdersFromAppendTrackingNumberModel
from qualer_sdk.models.qualer_api_models_service_orders_from_update_shipment_status_model import QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel as QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel

class ServiceOrderShipmentsApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def append_shipment_tracking_number(self, service_order_id: StrictInt, model: QualerApiModelsServiceOrdersFromAppendTrackingNumberModel, **kwargs) -> object: ...
    @validate_arguments
    def append_shipment_tracking_number_with_http_info(self, service_order_id: StrictInt, model: QualerApiModelsServiceOrdersFromAppendTrackingNumberModel, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def update_shipment_status(self, service_order_id: StrictInt, model: QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel, **kwargs) -> object: ...
    @validate_arguments
    def update_shipment_status_with_http_info(self, service_order_id: StrictInt, model: QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel, **kwargs) -> ApiResponse: ...
