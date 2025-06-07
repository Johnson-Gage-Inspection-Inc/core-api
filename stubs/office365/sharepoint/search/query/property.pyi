from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.search.query.property_value import QueryPropertyValue as QueryPropertyValue

class QueryProperty(ClientValue):
    Name: Incomplete
    Value: Incomplete
    def __init__(self, name: Incomplete | None = None, value=...) -> None: ...
    @property
    def entity_type_name(self): ...
