from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.planner.buckets.bucket import PlannerBucket as PlannerBucket
from office365.planner.plans.collection import (
    PlannerPlanCollection as PlannerPlanCollection,
)
from office365.planner.tasks.collection import (
    PlannerTaskCollection as PlannerTaskCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Planner(Entity):
    @property
    def buckets(self) -> EntityCollection[PlannerBucket]: ...
    @property
    def tasks(self) -> PlannerTaskCollection: ...
    @property
    def plans(self) -> PlannerPlanCollection: ...
