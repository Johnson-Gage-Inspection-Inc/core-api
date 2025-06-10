from _typeshed import Incomplete
from office365.runtime.client_object import ClientObject as ClientObject

class NotFoundException(Exception):
    entity: Incomplete
    query: Incomplete
    def __init__(self, entity: ClientObject = None, query: str = None) -> None: ...
