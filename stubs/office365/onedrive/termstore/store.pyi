from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.termstore.groups.collection import GroupCollection as GroupCollection
from office365.onedrive.termstore.sets.collection import SetCollection as SetCollection
from office365.onedrive.termstore.sets.set import Set as Set
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.types.collections import StringCollection as StringCollection

class Store(Entity):
    def get_all_term_sets(self): ...
    @property
    def default_language_tag(self) -> str | None: ...
    @property
    def language_tags(self): ...
    @property
    def groups(self) -> GroupCollection: ...
    @property
    def sets(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
