from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SPSiteCreationRequest(ClientValue):
    Title: Incomplete
    Url: Incomplete
    WebTemplate: Incomplete
    Owner: Incomplete
    Lcid: Incomplete
    ShareByEmailEnabled: bool
    Classification: str
    Description: str
    SiteDesignId: str
    HubSiteId: str
    WebTemplateExtensionId: str
    def __init__(
        self,
        title,
        url,
        owner: Incomplete | None = None,
        lcid: int = 1033,
        web_template: str = "SITEPAGEPUBLISHING#0",
    ) -> None: ...
    @property
    def entity_type_name(self): ...
