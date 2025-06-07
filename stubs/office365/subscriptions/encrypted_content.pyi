from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ChangeNotificationEncryptedContent(ClientValue):
    data: Incomplete
    dataKey: Incomplete
    dataSignature: Incomplete
    encryptionCertificateId: Incomplete
    encryptionCertificateThumbprint: Incomplete
    def __init__(self, data: Incomplete | None = None, data_key: Incomplete | None = None, data_signature: Incomplete | None = None, encryption_certificate_id: Incomplete | None = None, encryption_certificate_thumbprint: Incomplete | None = None) -> None: ...
