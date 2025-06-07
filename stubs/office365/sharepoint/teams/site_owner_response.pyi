from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class GetTeamChannelSiteOwnerResponse(ClientValue):
    Owner: Incomplete
    SecondaryContact: Incomplete
    def __init__(self, owner: Incomplete | None = None, secondary_contact: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
