from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.internal.paths.root import RootPath as RootPath
from office365.onedrive.internal.paths.site import SitePath as SitePath
from office365.onedrive.sites.site import Site as Site
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.queries.read_entity import ReadEntityQuery as ReadEntityQuery
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class SitesWithRoot(EntityCollection[Site]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_all_sites(self): ...
    def get_by_url(self, url): ...
    def remove(self, sites): ...
    def search(self, query_text: str) -> SitesWithRoot: ...
    @property
    def root(self) -> Site: ...
