from office365.entity import Entity as Entity
from office365.partners.billing.operation import Operation as Operation
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery

class BilledUsage(Entity):
    def export(self, invoice_id: str, attribute_set: str = None) -> Operation: ...
