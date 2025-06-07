from _typeshed import Incomplete
from office365.admin.admin import Admin as Admin
from office365.azure_env import AzureEnvironment as AzureEnvironment
from office365.booking.solutions.root import SolutionsRoot as SolutionsRoot
from office365.communications.cloud_communications import (
    CloudCommunications as CloudCommunications,
)
from office365.delta_collection import DeltaCollection as DeltaCollection
from office365.directory.applications.collection import (
    ApplicationCollection as ApplicationCollection,
)
from office365.directory.applications.template import (
    ApplicationTemplate as ApplicationTemplate,
)
from office365.directory.audit.log_root import AuditLogRoot as AuditLogRoot
from office365.directory.authentication.method_configuration import (
    AuthenticationMethodConfiguration as AuthenticationMethodConfiguration,
)
from office365.directory.certificates.auth_configuration import (
    CertificateBasedAuthConfiguration as CertificateBasedAuthConfiguration,
)
from office365.directory.directory import Directory as Directory
from office365.directory.domains.domain import Domain as Domain
from office365.directory.extensions.schema import SchemaExtension as SchemaExtension
from office365.directory.groups.collection import GroupCollection as GroupCollection
from office365.directory.groups.lifecycle_policy import (
    GroupLifecyclePolicy as GroupLifecyclePolicy,
)
from office365.directory.groups.setting_template import (
    GroupSettingTemplate as GroupSettingTemplate,
)
from office365.directory.identities.container import (
    IdentityContainer as IdentityContainer,
)
from office365.directory.identities.provider import IdentityProvider as IdentityProvider
from office365.directory.identitygovernance.governance import (
    IdentityGovernance as IdentityGovernance,
)
from office365.directory.internal.paths.me import MePath as MePath
from office365.directory.invitations.collection import (
    InvitationCollection as InvitationCollection,
)
from office365.directory.licenses.subscribed_sku import SubscribedSku as SubscribedSku
from office365.directory.object_collection import (
    DirectoryObjectCollection as DirectoryObjectCollection,
)
from office365.directory.permissions.grants.oauth2 import (
    OAuth2PermissionGrant as OAuth2PermissionGrant,
)
from office365.directory.permissions.grants.resource_specific import (
    ResourceSpecificPermissionGrant as ResourceSpecificPermissionGrant,
)
from office365.directory.policies.root import PolicyRoot as PolicyRoot
from office365.directory.protection.information import (
    InformationProtection as InformationProtection,
)
from office365.directory.protection.root import (
    IdentityProtectionRoot as IdentityProtectionRoot,
)
from office365.directory.rolemanagement.management import (
    RoleManagement as RoleManagement,
)
from office365.directory.rolemanagement.role import DirectoryRole as DirectoryRole
from office365.directory.security.security import Security as Security
from office365.directory.serviceprincipals.collection import (
    ServicePrincipalCollection as ServicePrincipalCollection,
)
from office365.directory.tenantinformation.relationship import (
    TenantRelationship as TenantRelationship,
)
from office365.directory.users.collection import UserCollection as UserCollection
from office365.directory.users.user import User as User
from office365.education.root import EducationRoot as EducationRoot
from office365.entity_collection import EntityCollection as EntityCollection
from office365.graph_request import GraphRequest as GraphRequest
from office365.intune.devices.app_management import (
    DeviceAppManagement as DeviceAppManagement,
)
from office365.intune.devices.collection import DeviceCollection as DeviceCollection
from office365.intune.devices.management.management import (
    DeviceManagement as DeviceManagement,
)
from office365.intune.organizations.contact import OrgContact as OrgContact
from office365.intune.organizations.organization import Organization as Organization
from office365.onedrive.drives.drive import Drive as Drive
from office365.onedrive.shares.collection import SharesCollection as SharesCollection
from office365.onedrive.sites.sites_with_root import SitesWithRoot as SitesWithRoot
from office365.onedrive.storage.storage import Storage as Storage
from office365.outlook.calendar.place import Place as Place
from office365.outlook.calendar.rooms.list import RoomList as RoomList
from office365.planner.planner import Planner as Planner
from office365.reports.root import ReportRoot as ReportRoot
from office365.runtime.client_runtime_context import (
    ClientRuntimeContext as ClientRuntimeContext,
)
from office365.runtime.http.http_method import HttpMethod as HttpMethod
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.odata.v4.batch_request import (
    ODataV4BatchRequest as ODataV4BatchRequest,
)
from office365.runtime.odata.v4.json_format import V4JsonFormat as V4JsonFormat
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.delete_entity import (
    DeleteEntityQuery as DeleteEntityQuery,
)
from office365.runtime.queries.update_entity import (
    UpdateEntityQuery as UpdateEntityQuery,
)
from office365.search.entity import SearchEntity as SearchEntity
from office365.search.external.external import External as External
from office365.subscriptions.collection import (
    SubscriptionCollection as SubscriptionCollection,
)
from office365.teams.apps.catalog import AppCatalogs as AppCatalogs
from office365.teams.chats.collection import ChatCollection as ChatCollection
from office365.teams.collection import TeamCollection as TeamCollection
from office365.teams.template import TeamsTemplate as TeamsTemplate
from office365.teams.viva.employee_experience import (
    EmployeeExperience as EmployeeExperience,
)
from typing import Any, Callable

class GraphClient(ClientRuntimeContext):
    def __init__(
        self,
        token_callback: Callable[[], dict] = None,
        tenant: str = None,
        scopes: list[str] = None,
        token_cache: Any = None,
        environment: str = ...,
    ) -> None: ...
    def with_certificate(self, client_id, thumbprint, private_key): ...
    def with_client_secret(self, client_id: str, client_secret: str) -> GraphClient: ...
    def with_token_interactive(
        self, client_id: str, username: str | None = None
    ) -> GraphClient: ...
    def with_username_and_password(
        self, client_id: str, username: str, password: str
    ) -> GraphClient: ...
    def execute_batch(
        self, items_per_batch: int = 20, success_callback: Incomplete | None = None
    ): ...
    def pending_request(self) -> GraphRequest: ...
    def service_root_url(self) -> str: ...
    @property
    def admin(self): ...
    @property
    def app_catalogs(self): ...
    @property
    def me(self): ...
    @property
    def device_management(self): ...
    @property
    def device_app_management(self): ...
    @property
    def drives(self): ...
    @property
    def users(self): ...
    @property
    def domains(self): ...
    @property
    def groups(self): ...
    @property
    def invitations(self): ...
    @property
    def identity_protection(self): ...
    @property
    def sites(self): ...
    @property
    def shares(self): ...
    @property
    def directory_objects(self): ...
    @property
    def devices(self): ...
    @property
    def teams(self): ...
    @property
    def chats(self): ...
    @property
    def group_setting_templates(self): ...
    @property
    def contacts(self): ...
    @property
    def directory(self): ...
    @property
    def directory_roles(self): ...
    @property
    def directory_role_templates(self): ...
    @property
    def identity_providers(self): ...
    @property
    def identity(self): ...
    @property
    def application_templates(self): ...
    @property
    def authentication_method_configurations(self): ...
    @property
    def applications(self): ...
    @property
    def certificate_based_auth_configuration(self): ...
    @property
    def service_principals(self): ...
    @property
    def organization(self): ...
    @property
    def subscribed_skus(self): ...
    @property
    def group_lifecycle_policies(self): ...
    @property
    def group_settings(self): ...
    @property
    def communications(self): ...
    @property
    def identity_governance(self): ...
    @property
    def information_protection(self): ...
    @property
    def storage(self): ...
    @property
    def subscriptions(self): ...
    @property
    def connections(self): ...
    @property
    def tenant_relationships(self): ...
    @property
    def audit_logs(self): ...
    @property
    def places(self): ...
    @property
    def oauth2_permission_grants(self): ...
    @property
    def room_lists(self): ...
    @property
    def reports(self): ...
    @property
    def role_management(self): ...
    @property
    def solutions(self): ...
    @property
    def teams_templates(self): ...
    @property
    def planner(self): ...
    @property
    def permission_grants(self): ...
    @property
    def print(self): ...
    @property
    def search(self): ...
    @property
    def employee_experience(self): ...
    @property
    def education(self): ...
    @property
    def policies(self): ...
    @property
    def external(self): ...
    @property
    def security(self): ...
    @property
    def schema_extensions(self): ...
