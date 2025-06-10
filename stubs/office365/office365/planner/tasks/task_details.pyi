from office365.entity import Entity as Entity
from office365.planner.external_references import (
    PlannerExternalReferences as PlannerExternalReferences,
)
from office365.planner.tasks.check_list_items import (
    PlannerChecklistItems as PlannerChecklistItems,
)

class PlannerTaskDetails(Entity):
    @property
    def checklist(self) -> PlannerChecklistItems: ...
    @property
    def description(self) -> str | None: ...
    @property
    def preview_type(self) -> str | None: ...
    @property
    def references(self) -> PlannerExternalReferences: ...
