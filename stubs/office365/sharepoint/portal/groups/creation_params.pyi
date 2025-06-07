from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class GroupCreationParams(ClientValue):
    Classification: Incomplete
    Description: Incomplete
    CreationOptions: Incomplete
    def __init__(self, classification: str = '', description: str = '') -> None: ...
    @property
    def entity_type_name(self): ...
