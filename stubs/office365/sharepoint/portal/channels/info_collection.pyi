from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.portal.channels.info import ChannelInfo as ChannelInfo

class ChannelInfoCollection(ClientValue):
    value: Incomplete
    def __init__(self, value: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
