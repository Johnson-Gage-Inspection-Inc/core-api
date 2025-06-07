from office365.runtime.client_object import ClientObject as ClientObject
from office365.runtime.queries.client_query import ClientQuery as ClientQuery

class DeleteEntityQuery(ClientQuery):
    def __init__(self, delete_type: ClientObject) -> None: ...
