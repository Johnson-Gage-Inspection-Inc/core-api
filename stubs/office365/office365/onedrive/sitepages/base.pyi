from _typeshed import Incomplete
from office365.onedrive.base_item import BaseItem as BaseItem
from office365.onedrive.driveitems.publication_facet import (
    PublicationFacet as PublicationFacet,
)

class BaseSitePage(BaseItem):
    @property
    def publishing_state(self) -> str | None: ...
    @property
    def page_layout(self) -> str | None: ...
    @property
    def title(self) -> str | None: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
