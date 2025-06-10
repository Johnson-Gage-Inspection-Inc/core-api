from _typeshed import Incomplete
from office365.sharepoint.sitedesigns.creation_info import (
    SiteDesignCreationInfo as SiteDesignCreationInfo,
)

class SiteDesignMetadata(SiteDesignCreationInfo):
    Order: Incomplete
    Version: Incomplete
    def __init__(
        self, order: Incomplete | None = None, version: Incomplete | None = None
    ) -> None: ...
    @property
    def entity_type_name(self): ...
