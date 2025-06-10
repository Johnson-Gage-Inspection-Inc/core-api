from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class PlannerGroup(Entity):
    @property
    def plans(self): ...
