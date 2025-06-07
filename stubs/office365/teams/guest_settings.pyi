from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class TeamGuestSettings(ClientValue):
    allowCreateUpdateChannels: Incomplete
    allowDeleteChannels: Incomplete
    def __init__(self, allow_create_update_channels: bool = True, allow_delete_channels: bool = True) -> None: ...
