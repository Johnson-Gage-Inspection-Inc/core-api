from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.planner.tasks.task import PlannerTask as PlannerTask
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class PlannerUser(Entity):
    @property
    def plans(self): ...
    @property
    def tasks(self) -> EntityCollection[PlannerTask]: ...
