from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.brandcenter.configuration import (
    BrandCenterConfiguration as BrandCenterConfiguration,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.sites.themes import SiteThemes as SiteThemes

class BrandCenter(Entity):
    def __init__(self, context) -> None: ...
    def configuration(self): ...
    def get_site_themes(self): ...
