from typing import TypeVar

from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.publishing.pages.metadata import (
    SitePageMetadata as SitePageMetadata,
)

T = TypeVar("T")

class SitePageMetadataCollection(EntityCollection[T]):
    def get_by_id(self, site_page_id): ...
