from _typeshed import Incomplete
from pydantic import (
    StrictInt as StrictInt,
    StrictStr as StrictStr,
    conlist as conlist,
    validate_arguments,
)
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import (
    ApiTypeError as ApiTypeError,
    ApiValueError as ApiValueError,
)
from qualer_sdk.models.qualer_api_models_asset_from_update_asset_class_model import (
    QualerApiModelsAssetFromUpdateAssetClassModel as QualerApiModelsAssetFromUpdateAssetClassModel,
)
from qualer_sdk.models.qualer_api_models_asset_from_update_asset_department_model import (
    QualerApiModelsAssetFromUpdateAssetDepartmentModel as QualerApiModelsAssetFromUpdateAssetDepartmentModel,
)
from qualer_sdk.models.qualer_api_models_asset_from_update_asset_room_model import (
    QualerApiModelsAssetFromUpdateAssetRoomModel as QualerApiModelsAssetFromUpdateAssetRoomModel,
)
from qualer_sdk.models.qualer_api_models_asset_from_update_room_model import (
    QualerApiModelsAssetFromUpdateRoomModel as QualerApiModelsAssetFromUpdateRoomModel,
)
from qualer_sdk.models.qualer_api_models_asset_to_asset_manage_response_model import (
    QualerApiModelsAssetToAssetManageResponseModel as QualerApiModelsAssetToAssetManageResponseModel,
)
from qualer_sdk.models.qualer_api_models_asset_to_asset_response_model import (
    QualerApiModelsAssetToAssetResponseModel as QualerApiModelsAssetToAssetResponseModel,
)
from qualer_sdk.models.qualer_api_models_asset_to_assets_count_response_model import (
    QualerApiModelsAssetToAssetsCountResponseModel as QualerApiModelsAssetToAssetsCountResponseModel,
)

class AssetsApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def clear_collected_assets(self, asset_ids: None, **kwargs) -> object: ...
    @validate_arguments
    def clear_collected_assets_with_http_info(
        self, asset_ids: None, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def collect_assets(self, asset_ids: None, **kwargs) -> object: ...
    @validate_arguments
    def collect_assets_with_http_info(
        self, asset_ids: None, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_all_assets(
        self, **kwargs
    ) -> list[QualerApiModelsAssetToAssetResponseModel]: ...
    @validate_arguments
    def get_all_assets_with_http_info(self, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def get_asset(
        self, id: StrictInt, **kwargs
    ) -> QualerApiModelsAssetToAssetResponseModel: ...
    @validate_arguments
    def get_asset_with_http_info(self, id: StrictInt, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def get_asset_by_asset_pool(
        self, asset_pool_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsAssetToAssetResponseModel]: ...
    @validate_arguments
    def get_asset_by_asset_pool_with_http_info(
        self, asset_pool_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_asset_by_asset_tag(
        self, asset_tag: StrictStr, **kwargs
    ) -> list[QualerApiModelsAssetToAssetResponseModel]: ...
    @validate_arguments
    def get_asset_by_asset_tag_with_http_info(
        self, asset_tag: StrictStr, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_asset_by_attribute(
        self,
        model_name: StrictStr | None = None,
        model_value: StrictStr | None = None,
        **kwargs,
    ) -> list[QualerApiModelsAssetToAssetResponseModel]: ...
    @validate_arguments
    def get_asset_by_attribute_with_http_info(
        self,
        model_name: StrictStr | None = None,
        model_value: StrictStr | None = None,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def get_asset_by_barcode(
        self, barcode: StrictStr, **kwargs
    ) -> list[QualerApiModelsAssetToAssetResponseModel]: ...
    @validate_arguments
    def get_asset_by_barcode_with_http_info(
        self, barcode: StrictStr, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_asset_by_serial_number(
        self, serial_number: StrictStr, **kwargs
    ) -> list[QualerApiModelsAssetToAssetResponseModel]: ...
    @validate_arguments
    def get_asset_by_serial_number_with_http_info(
        self, serial_number: StrictStr, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_asset_images(self, id: StrictInt, **kwargs) -> list[str]: ...
    @validate_arguments
    def get_asset_images_with_http_info(
        self, id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_asset_manager_counters(
        self, model_search_string: StrictStr | None = None, **kwargs
    ) -> QualerApiModelsAssetToAssetsCountResponseModel: ...
    @validate_arguments
    def get_asset_manager_counters_with_http_info(
        self, model_search_string: StrictStr | None = None, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_asset_manager_list(
        self,
        model_filter_type: StrictStr | None = None,
        model_search_string: StrictStr | None = None,
        model_page: StrictInt | None = None,
        model_page_size: StrictInt | None = None,
        **kwargs,
    ) -> list[QualerApiModelsAssetToAssetManageResponseModel]: ...
    @validate_arguments
    def get_asset_manager_list_with_http_info(
        self,
        model_filter_type: StrictStr | None = None,
        model_search_string: StrictStr | None = None,
        model_page: StrictInt | None = None,
        model_page_size: StrictInt | None = None,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def get_assets_by_equipment_id(
        self, equipment_id: StrictStr, **kwargs
    ) -> list[QualerApiModelsAssetToAssetResponseModel]: ...
    @validate_arguments
    def get_assets_by_equipment_id_with_http_info(
        self, equipment_id: StrictStr, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def post_asset_images(self, id: StrictInt, **kwargs) -> object: ...
    @validate_arguments
    def post_asset_images_with_http_info(
        self, id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def update_asset_class(
        self,
        id: StrictInt,
        model: QualerApiModelsAssetFromUpdateAssetClassModel,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def update_asset_class_with_http_info(
        self,
        id: StrictInt,
        model: QualerApiModelsAssetFromUpdateAssetClassModel,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def update_asset_department(
        self,
        id: StrictInt,
        model: QualerApiModelsAssetFromUpdateAssetDepartmentModel,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def update_asset_department_with_http_info(
        self,
        id: StrictInt,
        model: QualerApiModelsAssetFromUpdateAssetDepartmentModel,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def update_asset_room(
        self,
        id: StrictInt,
        model: QualerApiModelsAssetFromUpdateAssetRoomModel,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def update_asset_room_with_http_info(
        self,
        id: StrictInt,
        model: QualerApiModelsAssetFromUpdateAssetRoomModel,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def update_room(
        self, model: QualerApiModelsAssetFromUpdateRoomModel, **kwargs
    ) -> object: ...
    @validate_arguments
    def update_room_with_http_info(
        self, model: QualerApiModelsAssetFromUpdateRoomModel, **kwargs
    ) -> ApiResponse: ...
