from _typeshed import Incomplete
from office365.directory.domains.dns_record import DomainDnsRecord as DomainDnsRecord
from office365.directory.domains.state import DomainState as DomainState
from office365.directory.object_collection import (
    DirectoryObjectCollection as DirectoryObjectCollection,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.types.collections import StringCollection as StringCollection

class Domain(Entity):
    def verify(self): ...
    @property
    def supported_services(self): ...
    @property
    def domain_name_references(self): ...
    @property
    def service_configuration_records(self): ...
    @property
    def verification_dns_records(self): ...
    @property
    def state(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
