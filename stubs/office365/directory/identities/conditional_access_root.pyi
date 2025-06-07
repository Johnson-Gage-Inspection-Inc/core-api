from office365.directory.policies.conditional_access import ConditionalAccessPolicy as ConditionalAccessPolicy
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class ConditionalAccessRoot(Entity):
    @property
    def authentication_strength(self): ...
    @property
    def policies(self): ...
