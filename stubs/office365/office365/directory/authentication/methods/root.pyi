from _typeshed import Incomplete
from office365.directory.authentication.methods.details import (
    UserRegistrationDetails as UserRegistrationDetails,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.reports.userregistration.feature_summary import (
    UserRegistrationFeatureSummary as UserRegistrationFeatureSummary,
)
from office365.reports.userregistration.method_summary import (
    UserRegistrationMethodSummary as UserRegistrationMethodSummary,
)
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery

class AuthenticationMethodsRoot(Entity):
    def users_registered_by_feature(self): ...
    def users_registered_by_method(self): ...
    @property
    def user_registration_details(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
