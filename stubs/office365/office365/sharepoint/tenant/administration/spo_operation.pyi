from office365.runtime.client_object import ClientObject as ClientObject

class SpoOperation(ClientObject):
    @property
    def has_timedout(self) -> bool | None: ...
    @property
    def is_complete(self): ...
    @property
    def polling_interval_secs(self): ...
