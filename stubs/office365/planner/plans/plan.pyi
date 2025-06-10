from _typeshed import Incomplete
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.planner.buckets.bucket import PlannerBucket as PlannerBucket
from office365.planner.plans.container import (
    PlannerPlanContainer as PlannerPlanContainer,
)
from office365.planner.plans.details import PlannerPlanDetails as PlannerPlanDetails
from office365.planner.tasks.task import PlannerTask as PlannerTask
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class PlannerPlan(Entity):
    def delete_object(self): ...
    @property
    def container(self): ...
    @property
    def title(self) -> str | None: ...
    @property
    def created_by(self): ...
    @property
    def buckets(self) -> EntityCollection[PlannerBucket]: ...
    @property
    def details(self): ...
    @property
    def tasks(self) -> EntityCollection[PlannerTask]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
