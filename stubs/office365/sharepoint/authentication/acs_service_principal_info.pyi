from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class SPACSServicePrincipalInfo(ClientValue):
    ApplicationEndpointAuthorities: Incomplete
    DisplayName: Incomplete
    def __init__(self, application_endpoint_authorities: Incomplete | None = None, display_name: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
