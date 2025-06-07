from office365.intune.servicecommunications.announcement_base import ServiceAnnouncementBase as ServiceAnnouncementBase
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.function import FunctionQuery as FunctionQuery

class ServiceHealthIssue(ServiceAnnouncementBase):
    def incident_report(self): ...
