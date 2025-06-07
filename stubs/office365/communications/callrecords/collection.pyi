from _typeshed import Incomplete
from office365.communications.callrecords.call_record import CallRecord as CallRecord
from office365.communications.callrecords.direct_routing_log_row import DirectRoutingLogRow as DirectRoutingLogRow
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.queries.function import FunctionQuery as FunctionQuery

class CallRecordCollection(EntityCollection[CallRecord]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_direct_routing_calls(self, from_datetime: Incomplete | None = None, to_datetime: Incomplete | None = None): ...
