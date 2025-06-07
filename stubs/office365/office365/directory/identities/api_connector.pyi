from office365.directory.authentication.configuration_base import (
    ApiAuthenticationConfigurationBase as ApiAuthenticationConfigurationBase,
)
from office365.entity import Entity as Entity
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class IdentityApiConnector(Entity):
    def upload_client_certificate(self, pkcs12_value, password): ...
    @property
    def authentication_configuration(self): ...
