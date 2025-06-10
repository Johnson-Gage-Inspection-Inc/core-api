from _typeshed import Incomplete
from pydantic import StrictInt as StrictInt, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from qualer_sdk.models.qualer_api_models_asset_to_asset_forecast_api_response_model import QualerApiModelsAssetToAssetForecastApiResponseModel as QualerApiModelsAssetToAssetForecastApiResponseModel
from qualer_sdk.models.qualer_api_models_maintenance_plans_to_maintenance_plan_response import QualerApiModelsMaintenancePlansToMaintenancePlanResponse as QualerApiModelsMaintenancePlansToMaintenancePlanResponse

class ClientMaintenancePlansApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def get_maintenance_plan_assets(self, maintenance_plan_id: StrictInt, **kwargs) -> list[QualerApiModelsAssetToAssetForecastApiResponseModel]: ...
    @validate_arguments
    def get_maintenance_plan_assets_with_http_info(self, maintenance_plan_id: StrictInt, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def get_maintenance_plans_get2(self, client_company_id: StrictInt, **kwargs) -> list[QualerApiModelsMaintenancePlansToMaintenancePlanResponse]: ...
    @validate_arguments
    def get_maintenance_plans_get2_with_http_info(self, client_company_id: StrictInt, **kwargs) -> ApiResponse: ...
