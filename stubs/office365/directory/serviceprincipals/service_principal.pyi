from _typeshed import Incomplete
from office365.delta_collection import DeltaCollection as DeltaCollection
from office365.directory.applications.application import Application as Application
from office365.directory.applications.roles.assignment_collection import (
    AppRoleAssignmentCollection as AppRoleAssignmentCollection,
)
from office365.directory.applications.roles.collection import (
    AppRoleCollection as AppRoleCollection,
)
from office365.directory.applications.roles.role import AppRole as AppRole
from office365.directory.certificates.self_signed import (
    SelfSignedCertificate as SelfSignedCertificate,
)
from office365.directory.key_credential import KeyCredential as KeyCredential
from office365.directory.object import DirectoryObject as DirectoryObject
from office365.directory.object_collection import (
    DirectoryObjectCollection as DirectoryObjectCollection,
)
from office365.directory.password_credential import (
    PasswordCredential as PasswordCredential,
)
from office365.directory.permissions.grants.oauth2 import (
    OAuth2PermissionGrant as OAuth2PermissionGrant,
)
from office365.directory.permissions.scope import PermissionScope as PermissionScope
from office365.directory.synchronization.synchronization import (
    Synchronization as Synchronization,
)
from office365.directory.users.user import User as User
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.appid import AppIdPath as AppIdPath
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.types.collections import StringCollection as StringCollection
from typing_extensions import Self

class ServicePrincipal(DirectoryObject):
    def add_key(self, key_credential, password_credential, proof): ...
    def add_password(self, display_name: Incomplete | None = None): ...
    def add_token_signing_certificate(
        self, display_name, end_datetime: Incomplete | None = None
    ): ...
    def get_delegated_permissions(
        self, app: Application | str, principal: User | str = None
    ) -> ClientResult[StringCollection]: ...
    def grant_delegated_permissions(
        self, app: Application | str, principal: User | str | None, scope: AppRole | str
    ) -> Self: ...
    def revoke_delegated_permissions(
        self,
        app: Application | str,
        principal: User | str = None,
        scope: AppRole | str = None,
    ) -> Self: ...
    def get_application_permissions(
        self, app: Application | str
    ) -> ClientResult[AppRoleCollection]: ...
    def grant_application_permissions(
        self, app: Application | str, app_role: AppRole | str
    ) -> Self: ...
    def revoke_application_permissions(
        self, app: Application | str, app_role: AppRole | str
    ) -> Self: ...
    def remove_password(self, key_id): ...
    @property
    def account_enabled(self) -> bool | None: ...
    @property
    def alternative_names(self): ...
    @property
    def app_description(self) -> str | None: ...
    @property
    def app_display_name(self) -> str | None: ...
    @property
    def app_id(self) -> str | None: ...
    @property
    def app_role_assigned_to(self): ...
    @property
    def app_role_assignments(self): ...
    @property
    def app_roles(self): ...
    @property
    def display_name(self) -> str | None: ...
    @property
    def homepage(self) -> str | None: ...
    @property
    def key_credentials(self): ...
    @property
    def login_url(self) -> str | None: ...
    @property
    def logout_url(self) -> str | None: ...
    @property
    def notification_email_addresses(self): ...
    @property
    def service_principal_type(self) -> str | None: ...
    @property
    def owners(self): ...
    @property
    def oauth2_permission_scopes(self) -> ClientValueCollection[PermissionScope]: ...
    @property
    def oauth2_permission_grants(self) -> DeltaCollection[OAuth2PermissionGrant]: ...
    @property
    def created_objects(self): ...
    @property
    def owned_objects(self): ...
    @property
    def synchronization(self): ...
    @property
    def token_encryption_key_id(self) -> str | None: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
    def set_property(self, name, value, persist_changes: bool = True): ...
