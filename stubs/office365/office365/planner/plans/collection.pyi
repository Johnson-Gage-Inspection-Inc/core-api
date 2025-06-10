from _typeshed import Incomplete
from office365.directory.groups.group import Group as Group
from office365.entity_collection import EntityCollection as EntityCollection
from office365.planner.plans.plan import PlannerPlan as PlannerPlan
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)

class PlannerPlanCollection(EntityCollection[PlannerPlan]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, title: str, container: str | Group) -> PlannerPlan: ...
