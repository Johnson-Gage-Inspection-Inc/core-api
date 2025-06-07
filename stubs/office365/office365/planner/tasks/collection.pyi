from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.planner.plans.plan import PlannerPlan as PlannerPlan
from office365.planner.tasks.task import PlannerTask as PlannerTask
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)

class PlannerTaskCollection(EntityCollection[PlannerTask]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, title, plan, bucket: Incomplete | None = None): ...
