from office365.runtime.client_object import ClientObject as ClientObject
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.queries.client_query import ClientQuery as ClientQuery
from office365.runtime.queries.client_query import T as T

class CreateEntityQuery(ClientQuery[T]):
    def __init__(
        self,
        parent_entity: ClientObject,
        parameters: ClientObject | ClientValue | dict,
        return_type: T = None,
    ) -> None: ...
