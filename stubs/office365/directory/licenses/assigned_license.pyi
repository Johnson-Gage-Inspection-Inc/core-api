from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class AssignedLicense(ClientValue):
    skuId: Incomplete
    disabledPlans: Incomplete
    def __init__(self, sku_id: Incomplete | None = None, disabled_plans: Incomplete | None = None) -> None: ...
