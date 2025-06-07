from _typeshed import Incomplete
from office365.directory.security.cases.ediscovery import (
    EdiscoveryCase as EdiscoveryCase,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class CasesRoot(Entity):
    @property
    def ediscovery_cases(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
