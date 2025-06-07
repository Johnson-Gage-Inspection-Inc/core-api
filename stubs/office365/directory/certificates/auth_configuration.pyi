from office365.directory.certificates.authority import CertificateAuthority as CertificateAuthority
from office365.entity import Entity as Entity
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class CertificateBasedAuthConfiguration(Entity):
    @property
    def certificate_authorities(self): ...
