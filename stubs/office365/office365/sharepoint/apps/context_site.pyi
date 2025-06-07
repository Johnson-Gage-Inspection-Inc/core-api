from office365.onedrive.sites.site import Site as Site
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.webs.web import Web as Web

class AppContextSite(Entity):
    def __init__(self, context: ClientContext, site_url: str) -> None: ...
    @property
    def site(self): ...
    @property
    def web(self): ...
