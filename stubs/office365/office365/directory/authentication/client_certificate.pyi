from _typeshed import Incomplete
from office365.directory.authentication.configuration_base import (
    ApiAuthenticationConfigurationBase as ApiAuthenticationConfigurationBase,
)
from office365.directory.certificates.pkcs12_information import (
    Pkcs12CertificateInformation as Pkcs12CertificateInformation,
)
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class ClientCertificateAuthentication(ApiAuthenticationConfigurationBase):
    certificateList: Incomplete
    def __init__(self, certificates: Incomplete | None = None) -> None: ...
