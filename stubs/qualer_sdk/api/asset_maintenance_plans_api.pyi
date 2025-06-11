from _typeshed import Incomplete
from pydantic import StrictInt as StrictInt, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import (
    ApiTypeError as ApiTypeError,
    ApiValueError as ApiValueError,
)
from qualer_sdk.models.qualer_api_models_asset_from_update_asset_maintenance_service_dat import (
    QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat as QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat,
)
from qualer_sdk.models.qualer_api_models_asset_to_asset_maintenance_plan_model import (
    QualerApiModelsAssetToAssetMaintenancePlanModel as QualerApiModelsAssetToAssetMaintenancePlanModel,
)

class AssetMaintenancePlansApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def get_maintenance_plan(
        self, asset_id: StrictInt, maintenance_plan_id: StrictInt, **kwargs
    ) -> QualerApiModelsAssetToAssetMaintenancePlanModel: ...
    @validate_arguments
    def get_maintenance_plan_with_http_info(
        self, asset_id: StrictInt, maintenance_plan_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_maintenance_plans(
        self, asset_id: StrictInt, **kwargs
    ) -> QualerApiModelsAssetToAssetMaintenancePlanModel: ...
    @validate_arguments
    def get_maintenance_plans_with_http_info(
        self, asset_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def reset_initial_service_date(
        self,
        asset_id: StrictInt,
        maintenance_plan_id: StrictInt,
        model: QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def reset_initial_service_date_with_http_info(
        self,
        asset_id: StrictInt,
        maintenance_plan_id: StrictInt,
        model: QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat,
        **kwargs,
    ) -> ApiResponse: ...
