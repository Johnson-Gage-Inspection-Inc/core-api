from _typeshed import Incomplete
from office365.directory.authentication.strength_usage import AuthenticationStrengthUsage as AuthenticationStrengthUsage
from office365.directory.policies.update_allowed_combinations_result import UpdateAllowedCombinationsResult as UpdateAllowedCombinationsResult
from office365.entity import Entity as Entity
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery

class AuthenticationStrengthPolicy(Entity):
    def usage(self): ...
    def update_allowed_combinations(self, allowed_combinations: Incomplete | None = None): ...
