from _typeshed import Incomplete
from office365.directory.identitygovernance.appconsent.request_scope import AppConsentRequestScope as AppConsentRequestScope
from office365.directory.identitygovernance.userconsent.request_collection import UserConsentRequestCollection as UserConsentRequestCollection
from office365.entity import Entity as Entity
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class AppConsentRequest(Entity):
    @property
    def app_display_name(self) -> str | None: ...
    @property
    def app_id(self) -> str | None: ...
    @property
    def pending_scopes(self) -> ClientValueCollection[AppConsentRequestScope]: ...
    @property
    def user_consent_requests(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
