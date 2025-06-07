from _typeshed import Incomplete
from office365.communications.callrecords.collection import CallRecordCollection as CallRecordCollection
from office365.communications.calls.collection import CallCollection as CallCollection
from office365.communications.onlinemeetings.collection import OnlineMeetingCollection as OnlineMeetingCollection
from office365.communications.presences.presence import Presence as Presence
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery

class CloudCommunications(Entity):
    def get_presences_by_user_id(self, ids): ...
    @property
    def calls(self): ...
    @property
    def call_records(self): ...
    @property
    def online_meetings(self): ...
    @property
    def presences(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
