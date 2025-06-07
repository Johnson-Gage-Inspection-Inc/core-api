from _typeshed import Incomplete
from office365.directory.identitygovernance.userconsent.request import UserConsentRequest as UserConsentRequest
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.queries.function import FunctionQuery as FunctionQuery

class UserConsentRequestCollection(EntityCollection[UserConsentRequest]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def filter_by_current_user(self, on): ...
