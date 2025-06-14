from _typeshed import Incomplete
from office365.communications.calls.call import Call as Call
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class CallCollection(EntityCollection):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def create(self, callback_uri): ...
    def log_teleconference_device_quality(self, quality: Incomplete | None = None): ...
