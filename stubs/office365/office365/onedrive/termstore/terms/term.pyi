from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.internal.paths.children import ChildrenPath as ChildrenPath
from office365.onedrive.termstore.terms.description import (
    LocalizedDescription as LocalizedDescription,
)
from office365.onedrive.termstore.terms.label import LocalizedLabel as LocalizedLabel
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Term(Entity):
    @property
    def descriptions(self): ...
    @property
    def labels(self): ...
    @property
    def created_datetime(self): ...
    @property
    def children(self): ...
    @property
    def relations(self): ...
    @property
    def set(self): ...
    @property
    def entity_type_name(self) -> None: ...
