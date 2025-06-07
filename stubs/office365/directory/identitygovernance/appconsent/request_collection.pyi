from _typeshed import Incomplete
from office365.directory.identitygovernance.appconsent.request import AppConsentRequest as AppConsentRequest
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.queries.function import FunctionQuery as FunctionQuery

class AppConsentRequestCollection(EntityCollection[AppConsentRequest]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def filter_by_current_user(self, on): ...
