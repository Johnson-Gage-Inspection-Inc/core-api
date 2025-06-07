from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.planner.category_descriptions import PlannerCategoryDescriptions as PlannerCategoryDescriptions
from office365.planner.user_ids import PlannerUserIds as PlannerUserIds

class PlannerPlanDetails(Entity):
    @property
    def category_descriptions(self) -> PlannerCategoryDescriptions: ...
    @property
    def shared_with(self) -> PlannerUserIds: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
