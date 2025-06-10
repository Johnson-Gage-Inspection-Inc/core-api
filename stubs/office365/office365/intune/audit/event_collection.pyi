from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.intune.audit.event import AuditEvent as AuditEvent
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.types.collections import StringCollection as StringCollection

class AuditEventCollection(EntityCollection[AuditEvent]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_audit_categories(self): ...
    def get_audit_activity_types(self, category): ...
