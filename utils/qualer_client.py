# utils/qualer_client.py
from os import getenv

import qualer_sdk.models
from qualer_sdk import ApiClient, Configuration
from qualer_sdk.models.qualer_api_models_asset_attributes_to_asset_attributes_response import (
    QualerApiModelsAssetAttributesToAssetAttributesResponse,
)
from qualer_sdk.models.qualer_api_models_asset_service_records_to_asset_service_record_response_model import (
    QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel,
)
from qualer_sdk.models.qualer_api_models_asset_to_asset_response_model import (
    QualerApiModelsAssetToAssetResponseModel,
)
from qualer_sdk.models.qualer_api_models_clients_to_client_company_response_model import (
    QualerApiModelsClientsToClientCompanyResponseModel,
)

# Import and register model classes that the ApiClient expects to find
from qualer_sdk.models.qualer_api_models_clients_to_employee_response_model import (
    QualerApiModelsClientsToEmployeeResponseModel,
)
from qualer_sdk.models.qualer_api_models_service_orders_to_client_order_item_response_model import (
    QualerApiModelsServiceOrdersToClientOrderItemResponseModel,
)
from qualer_sdk.models.qualer_api_models_service_orders_to_client_order_response_model import (
    QualerApiModelsServiceOrdersToClientOrderResponseModel,
)

# Register models with the models module so ApiClient can find them
qualer_sdk.models.QualerApiModelsClientsToEmployeeResponseModel = (
    QualerApiModelsClientsToEmployeeResponseModel
)
qualer_sdk.models.QualerApiModelsClientsToClientCompanyResponseModel = (
    QualerApiModelsClientsToClientCompanyResponseModel
)
qualer_sdk.models.QualerApiModelsAssetToAssetResponseModel = (
    QualerApiModelsAssetToAssetResponseModel
)
qualer_sdk.models.QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel = (
    QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel
)
qualer_sdk.models.QualerApiModelsServiceOrdersToClientOrderResponseModel = (
    QualerApiModelsServiceOrdersToClientOrderResponseModel
)
qualer_sdk.models.QualerApiModelsServiceOrdersToClientOrderItemResponseModel = (
    QualerApiModelsServiceOrdersToClientOrderItemResponseModel
)
qualer_sdk.models.QualerApiModelsAssetAttributesToAssetAttributesResponse = (
    QualerApiModelsAssetAttributesToAssetAttributesResponse
)


def make_qualer_client() -> ApiClient:
    config = Configuration()
    config.host = "https://jgiquality.qualer.com"
    client = ApiClient(configuration=config)
    client.default_headers["Authorization"] = f'Api-Token {getenv("QUALER_API_KEY")}'
    return client
