from _typeshed import Incomplete
from office365.directory.identities.provider import IdentityProvider as IdentityProvider
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.types.collections import StringCollection as StringCollection

class IdentityProviderCollection(EntityCollection):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def available_provider_types(self): ...
