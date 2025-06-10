from _typeshed import Incomplete
from office365.directory.tenantinformation.information import (
    TenantInformation as TenantInformation,
)
from office365.directory.tenantinformation.multi_organization import (
    MultiTenantOrganization as MultiTenantOrganization,
)
from office365.entity import Entity as Entity
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery

class TenantRelationship(Entity):
    def find_tenant_information_by_domain_name(self, domain_name): ...
    def find_tenant_information_by_tenant_id(self, tenant_id): ...
    @property
    def multi_tenant_organization(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
