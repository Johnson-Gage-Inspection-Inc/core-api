from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.publishing.highlights_info import (
    HighlightsInfo as HighlightsInfo,
)
from office365.sharepoint.publishing.pages.page import SitePage as SitePage

class CampaignPublication(SitePage):
    def get_highlights_info(self): ...
    def send_test_email(self): ...
    @property
    def email_endpoint(self) -> str | None: ...
    @property
    def entity_type_name(self): ...
