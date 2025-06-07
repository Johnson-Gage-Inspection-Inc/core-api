from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class Pkcs12CertificateInformation(ClientValue):
    thumbprint: Incomplete
    isActive: Incomplete
    notAfter: Incomplete
    notBefore: Incomplete
    def __init__(self, thumbprint: Incomplete | None = None, is_active: Incomplete | None = None, not_after: Incomplete | None = None, not_before: Incomplete | None = None) -> None: ...
