from _typeshed import Incomplete
from office365.planner.tasks.check_list_item import PlannerChecklistItem as PlannerChecklistItem
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class PlannerChecklistItems(ClientValueCollection):
    def __init__(self, initial_values: Incomplete | None = None) -> None: ...
