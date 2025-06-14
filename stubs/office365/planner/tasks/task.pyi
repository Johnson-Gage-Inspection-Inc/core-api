from _typeshed import Incomplete
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.entity import Entity as Entity
from office365.planner.tasks.task_details import (
    PlannerTaskDetails as PlannerTaskDetails,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class PlannerTask(Entity):
    @property
    def created_by(self): ...
    @property
    def created_datetime(self): ...
    @property
    def title(self): ...
    @property
    def details(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
