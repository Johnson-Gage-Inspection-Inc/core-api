from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ProvisionedTemporaryAzureContainerInfo(ClientValue):
    EncryptionKey: Incomplete
    Uri: Incomplete
    def __init__(
        self, encryption_key: Incomplete | None = None, uri: Incomplete | None = None
    ) -> None: ...
