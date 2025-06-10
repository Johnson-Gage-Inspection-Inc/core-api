from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.planner.tasks.task import PlannerTask as PlannerTask
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class PlannerBucket(Entity):
    @property
    def tasks(self): ...
