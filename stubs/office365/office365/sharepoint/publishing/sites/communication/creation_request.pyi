from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class CommunicationSiteCreationRequest(ClientValue):
    Title: Incomplete
    Url: Incomplete
    Description: Incomplete
    lcid: Incomplete
    Classification: Incomplete
    AllowFileSharingForGuestUsers: Incomplete
    WebTemplateExtensionId: Incomplete
    SiteDesignId: Incomplete
    def __init__(
        self,
        title,
        url,
        description: Incomplete | None = None,
        lcid: Incomplete | None = None,
        classification: Incomplete | None = None,
        allow_filesharing_for_guest_users: Incomplete | None = None,
        web_template_extension_id: Incomplete | None = None,
        site_design_id: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
