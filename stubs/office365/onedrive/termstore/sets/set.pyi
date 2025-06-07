from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.internal.paths.children import ChildrenPath as ChildrenPath
from office365.onedrive.termstore.relation import Relation as Relation
from office365.onedrive.termstore.sets.name import LocalizedName as LocalizedName
from office365.onedrive.termstore.terms.collection import TermCollection as TermCollection
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Set(Entity):
    @property
    def children(self) -> TermCollection: ...
    @property
    def localized_names(self) -> ClientValueCollection[LocalizedName]: ...
    @property
    def parent_group(self): ...
    @property
    def relations(self) -> EntityCollection[Relation]: ...
    @property
    def terms(self) -> TermCollection: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
    @property
    def entity_type_name(self) -> None: ...
