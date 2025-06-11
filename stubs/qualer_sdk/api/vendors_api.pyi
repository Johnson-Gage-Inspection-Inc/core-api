from _typeshed import Incomplete
from datetime import datetime
from pydantic import (
    Field as Field,
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
from qualer_sdk.models.qualer_api_models_vendors_from_sponsored_vendor_create_model import (
    QualerApiModelsVendorsFromSponsoredVendorCreateModel as QualerApiModelsVendorsFromSponsoredVendorCreateModel,
)
from qualer_sdk.models.qualer_api_models_vendors_from_sponsored_vendor_edit_model import (
    QualerApiModelsVendorsFromSponsoredVendorEditModel as QualerApiModelsVendorsFromSponsoredVendorEditModel,
)
from qualer_sdk.models.qualer_api_models_vendors_to_created_vendor_company_response import (
    QualerApiModelsVendorsToCreatedVendorCompanyResponse as QualerApiModelsVendorsToCreatedVendorCompanyResponse,
)
from qualer_sdk.models.qualer_api_models_vendors_to_vendor_company_response_model import (
    QualerApiModelsVendorsToVendorCompanyResponseModel as QualerApiModelsVendorsToVendorCompanyResponseModel,
)
from typing_extensions import Annotated

class VendorsApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def create_post3(
        self,
        model: Annotated[QualerApiModelsVendorsFromSponsoredVendorCreateModel, None],
        **kwargs,
    ) -> QualerApiModelsVendorsToCreatedVendorCompanyResponse: ...
    @validate_arguments
    def create_post3_with_http_info(
        self,
        model: Annotated[QualerApiModelsVendorsFromSponsoredVendorCreateModel, None],
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def get_all_get3(
        self,
        model_account_number_text: StrictStr | None = None,
        model_company_name: StrictStr | None = None,
        model_take: StrictInt | None = None,
        model_modified_after: datetime | None = None,
        **kwargs,
    ) -> list[QualerApiModelsVendorsToVendorCompanyResponseModel]: ...
    @validate_arguments
    def get_all_get3_with_http_info(
        self,
        model_account_number_text: StrictStr | None = None,
        model_company_name: StrictStr | None = None,
        model_take: StrictInt | None = None,
        model_modified_after: datetime | None = None,
        **kwargs,
    ) -> ApiResponse: ...
    @validate_arguments
    def get_get8(
        self, vendor_company_id: StrictInt, **kwargs
    ) -> QualerApiModelsVendorsToVendorCompanyResponseModel: ...
    @validate_arguments
    def get_get8_with_http_info(
        self, vendor_company_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def update_put4(
        self,
        model: Annotated[QualerApiModelsVendorsFromSponsoredVendorEditModel, None],
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def update_put4_with_http_info(
        self,
        model: Annotated[QualerApiModelsVendorsFromSponsoredVendorEditModel, None],
        **kwargs,
    ) -> ApiResponse: ...
