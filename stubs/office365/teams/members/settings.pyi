from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class TeamMemberSettings(ClientValue):
    allowCreateUpdateChannels: Incomplete
    allowDeleteChannels: bool
    allowAddRemoveApps: bool
    allowCreateUpdateRemoveTabs: bool
    allowCreateUpdateRemoveConnectors: bool
    def __init__(self, allow_create_update_channels: Incomplete | None = None) -> None: ...
