from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class CertificateAuthority(ClientValue):
    certificate: Incomplete
    certificateRevocationListUrl: Incomplete
    isRootAuthority: Incomplete
    issuer: Incomplete
    issuerSki: Incomplete
    def __init__(
        self,
        certificate: Incomplete | None = None,
        certificate_revocation_list_url: Incomplete | None = None,
        is_root_authority: Incomplete | None = None,
        issuer: Incomplete | None = None,
        issuer_ski: Incomplete | None = None,
    ) -> None: ...
