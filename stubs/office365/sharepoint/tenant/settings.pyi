from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class TenantSettings(Entity):
    def clear_corporate_catalog(self): ...
    def get_data_access_governance_report_config(self): ...
    def set_corporate_catalog(self, url): ...
    @property
    def corporate_catalog_url(self) -> str | None: ...
    @staticmethod
    def current(context): ...
