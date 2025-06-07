from _typeshed import Incomplete
from office365.directory.certificates.auth_configuration import (
    CertificateBasedAuthConfiguration as CertificateBasedAuthConfiguration,
)
from office365.directory.domains.verified import VerifiedDomain as VerifiedDomain
from office365.directory.extensions.extension import Extension as Extension
from office365.directory.licenses.assigned_plan import AssignedPlan as AssignedPlan
from office365.directory.object import DirectoryObject as DirectoryObject
from office365.entity_collection import EntityCollection as EntityCollection
from office365.intune.organizations.branding import (
    OrganizationalBranding as OrganizationalBranding,
)
from office365.intune.provisioned_plan import ProvisionedPlan as ProvisionedPlan
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.types.collections import StringCollection as StringCollection

class Organization(DirectoryObject):
    @property
    def assigned_plans(self): ...
    @property
    def branding(self): ...
    @property
    def business_phones(self): ...
    @property
    def extensions(self) -> EntityCollection[Extension]: ...
    @property
    def certificate_based_auth_configuration(self): ...
    @property
    def provisioned_plans(self): ...
    @property
    def verified_domains(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
