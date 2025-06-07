from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class PendingReviewItemsStatistics(ClientValue):
    LabelId: Incomplete
    LabelName: Incomplete
    def __init__(self, label_id: Incomplete | None = None, label_name: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
