from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SensitivityLabelAssignment(ClientValue):
    assignmentMethod: Incomplete
    sensitivityLabelId: Incomplete
    tenantId: Incomplete
    def __init__(self, assignment_method: Incomplete | None = None, sensitivity_label_id: Incomplete | None = None, tenant_id: Incomplete | None = None) -> None: ...
