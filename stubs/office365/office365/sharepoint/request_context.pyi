from office365.runtime.client_object import ClientObject as ClientObject
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class RequestContext(ClientObject):
    def get_remote_context(self): ...
