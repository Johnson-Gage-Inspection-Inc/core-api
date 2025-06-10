from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class SiteIconManager(Entity):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_site_logo(
        self,
        site_url,
        target: Incomplete | None = None,
        _type: Incomplete | None = None,
        return_type: Incomplete | None = None,
    ): ...
    def set_site_logo(
        self,
        relative_logo_url,
        _type: Incomplete | None = None,
        aspect: Incomplete | None = None,
        focalx: Incomplete | None = None,
        focaly: Incomplete | None = None,
        isFocalPatch: Incomplete | None = None,
    ): ...
    @property
    def entity_type_name(self): ...
