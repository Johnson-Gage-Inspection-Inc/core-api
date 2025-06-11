from _typeshed import Incomplete
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
from qualer_sdk.models.qualer_api_models_company_to_departments_response_model import (
    QualerApiModelsCompanyToDepartmentsResponseModel as QualerApiModelsCompanyToDepartmentsResponseModel,
)
from qualer_sdk.models.qualer_api_models_company_to_environment_response_model import (
    QualerApiModelsCompanyToEnvironmentResponseModel as QualerApiModelsCompanyToEnvironmentResponseModel,
)
from qualer_sdk.models.qualer_api_models_company_to_sites_response_model import (
    QualerApiModelsCompanyToSitesResponseModel as QualerApiModelsCompanyToSitesResponseModel,
)
from qualer_sdk.models.qualer_web_mvc_areas_api_models_company_from_add_department_model import (
    QualerWebMvcAreasApiModelsCompanyFromAddDepartmentModel as QualerWebMvcAreasApiModelsCompanyFromAddDepartmentModel,
)
from qualer_sdk.models.qualer_web_mvc_areas_api_models_company_from_update_department_model import (
    QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel as QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel,
)
from typing_extensions import Annotated

class CompanyApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    @validate_arguments
    def add_department(
        self, model: QualerWebMvcAreasApiModelsCompanyFromAddDepartmentModel, **kwargs
    ) -> object: ...
    @validate_arguments
    def add_department_with_http_info(
        self, model: QualerWebMvcAreasApiModelsCompanyFromAddDepartmentModel, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def delete_department(self, department_id: StrictInt, **kwargs) -> object: ...
    @validate_arguments
    def delete_department_with_http_info(
        self, department_id: StrictInt, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def departments(
        self, **kwargs
    ) -> list[QualerApiModelsCompanyToDepartmentsResponseModel]: ...
    @validate_arguments
    def departments_with_http_info(self, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def lookups(self, lookup_type: StrictStr, **kwargs) -> list[str]: ...
    @validate_arguments
    def lookups_with_http_info(
        self, lookup_type: StrictStr, **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def site_rooms(
        self, id: Annotated[StrictInt, None], **kwargs
    ) -> list[QualerApiModelsCompanyToEnvironmentResponseModel]: ...
    @validate_arguments
    def site_rooms_with_http_info(
        self, id: Annotated[StrictInt, None], **kwargs
    ) -> ApiResponse: ...
    @validate_arguments
    def sites(self, **kwargs) -> list[QualerApiModelsCompanyToSitesResponseModel]: ...
    @validate_arguments
    def sites_with_http_info(self, **kwargs) -> ApiResponse: ...
    @validate_arguments
    def update_department(
        self,
        department_id: StrictInt,
        model: QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel,
        **kwargs,
    ) -> object: ...
    @validate_arguments
    def update_department_with_http_info(
        self,
        department_id: StrictInt,
        model: QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel,
        **kwargs,
    ) -> ApiResponse: ...
