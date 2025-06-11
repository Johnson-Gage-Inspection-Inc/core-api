from _typeshed import Incomplete
from pydantic import StrictInt as StrictInt, conlist as conlist, validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import (
    ApiTypeError as ApiTypeError,
    ApiValueError as ApiValueError,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_asset_attribute_response import (
    QualerApiModelsReportDatasetsToAssetAttributeResponse as QualerApiModelsReportDatasetsToAssetAttributeResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_asset_summary_response import (
    QualerApiModelsReportDatasetsToAssetSummaryResponse as QualerApiModelsReportDatasetsToAssetSummaryResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_client_attribute_response import (
    QualerApiModelsReportDatasetsToClientAttributeResponse as QualerApiModelsReportDatasetsToClientAttributeResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_company_certification_response import (
    QualerApiModelsReportDatasetsToCompanyCertificationResponse as QualerApiModelsReportDatasetsToCompanyCertificationResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_external_data_report_response import (
    QualerApiModelsReportDatasetsToExternalDataReportResponse as QualerApiModelsReportDatasetsToExternalDataReportResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_measurement_all_response import (
    QualerApiModelsReportDatasetsToMeasurementAllResponse as QualerApiModelsReportDatasetsToMeasurementAllResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_measurement_channel_result_response import (
    QualerApiModelsReportDatasetsToMeasurementChannelResultResponse as QualerApiModelsReportDatasetsToMeasurementChannelResultResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_measurement_channel_uniformity_response import (
    QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse as QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_measurement_chart_response import (
    QualerApiModelsReportDatasetsToMeasurementChartResponse as QualerApiModelsReportDatasetsToMeasurementChartResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_measurement_field_response import (
    QualerApiModelsReportDatasetsToMeasurementFieldResponse as QualerApiModelsReportDatasetsToMeasurementFieldResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_measurement_response import (
    QualerApiModelsReportDatasetsToMeasurementResponse as QualerApiModelsReportDatasetsToMeasurementResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_order_item_image_response import (
    QualerApiModelsReportDatasetsToOrderItemImageResponse as QualerApiModelsReportDatasetsToOrderItemImageResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_reference_standard_response import (
    QualerApiModelsReportDatasetsToReferenceStandardResponse as QualerApiModelsReportDatasetsToReferenceStandardResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_service_order_assignee_response import (
    QualerApiModelsReportDatasetsToServiceOrderAssigneeResponse as QualerApiModelsReportDatasetsToServiceOrderAssigneeResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_service_order_charge_response import (
    QualerApiModelsReportDatasetsToServiceOrderChargeResponse as QualerApiModelsReportDatasetsToServiceOrderChargeResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_service_order_item_component_response import (
    QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse as QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_service_order_item_field_response import (
    QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse as QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_service_order_item_option_response import (
    QualerApiModelsReportDatasetsToServiceOrderItemOptionResponse as QualerApiModelsReportDatasetsToServiceOrderItemOptionResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_service_order_item_response import (
    QualerApiModelsReportDatasetsToServiceOrderItemResponse as QualerApiModelsReportDatasetsToServiceOrderItemResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_service_order_item_status_history_response import (
    QualerApiModelsReportDatasetsToServiceOrderItemStatusHistoryResponse as QualerApiModelsReportDatasetsToServiceOrderItemStatusHistoryResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_service_order_item_task_response import (
    QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse as QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_service_order_response import (
    QualerApiModelsReportDatasetsToServiceOrderResponse as QualerApiModelsReportDatasetsToServiceOrderResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_service_order_task_response import (
    QualerApiModelsReportDatasetsToServiceOrderTaskResponse as QualerApiModelsReportDatasetsToServiceOrderTaskResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_tool_attribute_response import (
    QualerApiModelsReportDatasetsToToolAttributeResponse as QualerApiModelsReportDatasetsToToolAttributeResponse,
)
from qualer_sdk.models.qualer_api_models_report_datasets_to_tool_range_attribute_response import (
    QualerApiModelsReportDatasetsToToolRangeAttributeResponse as QualerApiModelsReportDatasetsToToolRangeAttributeResponse,
)

class ReportDatasetsApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def channel_uniformity_by_order(
        self, service_order_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse]: ...
    @validate_arguments
    def channel_uniformity_by_order_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_all_measurements(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToMeasurementAllResponse]: ...
    @validate_arguments
    def get_all_measurements_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_all_measurements_by_order(
        self, service_order_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToMeasurementAllResponse]: ...
    @validate_arguments
    def get_all_measurements_by_order_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_as_found_measurements(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToMeasurementResponse]: ...
    @validate_arguments
    def get_as_found_measurements_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_as_found_measurements_by_order(
        self, service_order_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToMeasurementResponse]: ...
    @validate_arguments
    def get_as_found_measurements_by_order_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_as_left_measurements(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToMeasurementResponse]: ...
    @validate_arguments
    def get_as_left_measurements_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_as_left_measurements_by_order(
        self, service_order_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToMeasurementResponse]: ...
    @validate_arguments
    def get_as_left_measurements_by_order_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_asset_attributes_get3(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToAssetAttributeResponse]: ...
    @validate_arguments
    def get_asset_attributes_get3_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_asset_service_records_get2(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> QualerApiModelsReportDatasetsToAssetSummaryResponse: ...
    @validate_arguments
    def get_asset_service_records_get2_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_channel_results(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToMeasurementChannelResultResponse]: ...
    @validate_arguments
    def get_channel_results_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_channel_results_by_order(
        self, service_order_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToMeasurementChannelResultResponse]: ...
    @validate_arguments
    def get_channel_results_by_order_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_channel_uniformity(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse]: ...
    @validate_arguments
    def get_channel_uniformity_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_client_attributes_get2(
        self, service_order_id: StrictInt, **kwargs
    ) -> QualerApiModelsReportDatasetsToClientAttributeResponse: ...
    @validate_arguments
    def get_client_attributes_get2_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_company_certifications(
        self, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToCompanyCertificationResponse]: ...
    @validate_arguments
    def get_company_certifications_with_http_info(self, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def get_external_data_reports(
        self, service_order_id: StrictInt, service_order_item_ids: None, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToExternalDataReportResponse]: ...
    @validate_arguments
    def get_external_data_reports_with_http_info(
        self, service_order_id: StrictInt, service_order_item_ids: None, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_measurement_charts(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToMeasurementChartResponse]: ...
    @validate_arguments
    def get_measurement_charts_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_measurement_fields(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToMeasurementFieldResponse]: ...
    @validate_arguments
    def get_measurement_fields_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_measurement_fields_by_order(
        self, service_order_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToMeasurementFieldResponse]: ...
    @validate_arguments
    def get_measurement_fields_by_order_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_order_item_documents(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToOrderItemImageResponse]: ...
    @validate_arguments
    def get_order_item_documents_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_order_item_images(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToOrderItemImageResponse]: ...
    @validate_arguments
    def get_order_item_images_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_reference_standards(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToReferenceStandardResponse]: ...
    @validate_arguments
    def get_reference_standards_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_reference_standards_by_order(
        self, service_order_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToReferenceStandardResponse]: ...
    @validate_arguments
    def get_reference_standards_by_order_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_service_order_assignees(
        self, service_order_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToServiceOrderAssigneeResponse]: ...
    @validate_arguments
    def get_service_order_assignees_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_service_order_charges(
        self, service_order_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToServiceOrderChargeResponse]: ...
    @validate_arguments
    def get_service_order_charges_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_service_order_item_components(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse]: ...
    @validate_arguments
    def get_service_order_item_components_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_service_order_item_components_by_order(
        self, service_order_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse]: ...
    @validate_arguments
    def get_service_order_item_components_by_order_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_service_order_item_fields_by_order(
        self, service_order_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse]: ...
    @validate_arguments
    def get_service_order_item_fields_by_order_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_service_order_item_options(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToServiceOrderItemOptionResponse]: ...
    @validate_arguments
    def get_service_order_item_options_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_service_order_item_status_history_async(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToServiceOrderItemStatusHistoryResponse]: ...
    @validate_arguments
    def get_service_order_item_status_history_async_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_service_order_item_tasks_by_order(
        self, service_order_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse]: ...
    @validate_arguments
    def get_service_order_item_tasks_by_order_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_service_order_item_tasks_by_order_items(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse]: ...
    @validate_arguments
    def get_service_order_item_tasks_by_order_items_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_service_order_items(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToServiceOrderItemResponse]: ...
    @validate_arguments
    def get_service_order_items_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_service_order_items_by_order(
        self, service_order_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToServiceOrderItemResponse]: ...
    @validate_arguments
    def get_service_order_items_by_order_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_service_order_tasks(
        self, service_order_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToServiceOrderTaskResponse]: ...
    @validate_arguments
    def get_service_order_tasks_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_service_orders(
        self, service_order_id: StrictInt, **kwargs
    ) -> QualerApiModelsReportDatasetsToServiceOrderResponse: ...
    @validate_arguments
    def get_service_orders_with_http_info(
        self, service_order_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_tool_attributes(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToToolAttributeResponse]: ...
    @validate_arguments
    def get_tool_attributes_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def get_tool_range_attributes(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> list[QualerApiModelsReportDatasetsToToolRangeAttributeResponse]: ...
    @validate_arguments
    def get_tool_range_attributes_with_http_info(
        self, service_order_item_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
