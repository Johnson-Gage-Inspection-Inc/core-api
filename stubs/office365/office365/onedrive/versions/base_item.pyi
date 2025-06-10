from _typeshed import Incomplete
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.entity import Entity as Entity
from office365.onedrive.driveitems.publication_facet import (
    PublicationFacet as PublicationFacet,
)

class BaseItemVersion(Entity):
    @property
    def last_modified_by(self): ...
    @property
    def last_modified_datetime(self): ...
    @property
    def publication(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
