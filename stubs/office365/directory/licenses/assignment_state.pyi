from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class LicenseAssignmentState(ClientValue):
    assignedByGroup: Incomplete
    disabledPlans: Incomplete
    error: Incomplete
    lastUpdatedDateTime: Incomplete
    skuId: Incomplete
    state: Incomplete
    def __init__(self, assigned_by_group: Incomplete | None = None, disabled_plans: Incomplete | None = None, error: Incomplete | None = None, last_updated_datetime: Incomplete | None = None, sku_id: Incomplete | None = None, state: Incomplete | None = None) -> None: ...
