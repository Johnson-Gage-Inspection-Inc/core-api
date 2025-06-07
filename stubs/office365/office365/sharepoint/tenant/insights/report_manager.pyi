from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.tenant.insights.report_metadata import (
    SPTenantIBInsightsReportMetadata as SPTenantIBInsightsReportMetadata,
)

class SPTenantIBInsightsReportManager(Entity):
    def __init__(self, context) -> None: ...
    def create_report(self): ...
    @property
    def entity_type_name(self): ...
