from _typeshed import Incomplete
from pydantic import validate_arguments
from qualer_sdk.api_client import ApiClient as ApiClient
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from qualer_sdk.models.qualer_api_models_reference_to_measurement_quantity_response import QualerApiModelsReferenceToMeasurementQuantityResponse as QualerApiModelsReferenceToMeasurementQuantityResponse
from qualer_sdk.models.qualer_api_models_reference_to_unit_of_measure_response import QualerApiModelsReferenceToUnitOfMeasureResponse as QualerApiModelsReferenceToUnitOfMeasureResponse

class ReferenceApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def get_measurement_quantities(self, **kwargs) -> list[QualerApiModelsReferenceToMeasurementQuantityResponse]: ...
    @validate_arguments
    def get_measurement_quantities_with_http_info(self, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def get_units_of_measure(self, **kwargs) -> list[QualerApiModelsReferenceToUnitOfMeasureResponse]: ...
    @validate_arguments
    def get_units_of_measure_with_http_info(self, **kwargs) -> ApiResponse: ...
