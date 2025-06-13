from typing import Callable

from office365.runtime.auth.client_credential import (
    ClientCredential as ClientCredential,
)
from office365.runtime.auth.user_credential import UserCredential as UserCredential
from office365.runtime.client_object import ClientObject as ClientObject
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.v3.entity import EntityPath as EntityPath
from office365.runtime.queries.delete_entity import (
    DeleteEntityQuery as DeleteEntityQuery,
)
from office365.runtime.queries.update_entity import (
    UpdateEntityQuery as UpdateEntityQuery,
)
from office365.sharepoint.client_context import ClientContext as ClientContext
from typing_extensions import Self

class Entity(ClientObject):
    def execute_query_with_incremental_retry(self, max_retry: int = 5): ...
    def execute_batch(
        self,
        items_per_batch: int = 100,
        success_callback: Callable[[list[ClientObject | ClientResult]], None] = None,
    ) -> Self: ...
    def with_credentials(
        self, credentials: UserCredential | ClientCredential
    ) -> Self: ...
    def delete_object(self): ...
    def update(self, *args): ...
    @property
    def context(self) -> ClientContext: ...
    @property
    def entity_type_name(self): ...
    @property
    def property_ref_name(self): ...
    def set_property(self, name, value, persist_changes: bool = True): ...
