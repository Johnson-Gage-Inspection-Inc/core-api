from _typeshed import Incomplete
from office365.directory.synchronization.error import (
    SynchronizationError as SynchronizationError,
)
from office365.runtime.client_value import ClientValue as ClientValue

class SynchronizationQuarantine(ClientValue):
    error: Incomplete
    def __init__(self, error=...) -> None: ...
