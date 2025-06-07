from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.tenant.administration.audit.data import AuditData as AuditData

class UnifiedAuditRecord(ClientValue):
    AuditData: Incomplete
    CreationDate: Incomplete
    Operation: Incomplete
    RecordId: Incomplete
    RecordType: Incomplete
    UserId: Incomplete
    def __init__(
        self,
        audit_data=...,
        creation_date: Incomplete | None = None,
        operation: Incomplete | None = None,
        record_id: Incomplete | None = None,
        record_type: Incomplete | None = None,
        user_id: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
