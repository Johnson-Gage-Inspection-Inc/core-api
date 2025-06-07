from office365.sharepoint.publishing.pages.metadata import (
    SitePageMetadata as SitePageMetadata,
)

class RepostPageMetadata(SitePageMetadata):
    @property
    def entity_type_name(self): ...
