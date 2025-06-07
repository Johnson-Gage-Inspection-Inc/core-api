from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.tenant.administration.modified_property import ModifiedProperty as ModifiedProperty

class AuditData(ClientValue):
    ClientIP: Incomplete
    CorrelationId: Incomplete
    ModifiedProperties: Incomplete
    def __init__(self, client_ip: Incomplete | None = None, correlation_id: Incomplete | None = None, modified_properties: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
