from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.sharing.reports.site_capabilities import SiteSharingReportCapabilities as SiteSharingReportCapabilities
from office365.sharepoint.sharing.site_sharing_report_status import SiteSharingReportStatus as SiteSharingReportStatus

class SiteSharingReportHelper(Entity):
    @staticmethod
    def cancel_sharing_report_job(context: ClientContext) -> ClientResult[SiteSharingReportStatus]: ...
    @staticmethod
    def create_sharing_report_job(context, web_url, folder_url): ...
    @staticmethod
    def get_site_sharing_report_capabilities(context): ...
    @property
    def entity_type_name(self): ...
