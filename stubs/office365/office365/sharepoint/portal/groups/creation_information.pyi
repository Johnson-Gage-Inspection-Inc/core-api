from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.portal.groups.creation_params import (
    GroupCreationParams as GroupCreationParams,
)

class GroupCreationInformation(ClientValue):
    displayName: Incomplete
    alias: Incomplete
    isPublic: Incomplete
    optionalParams: Incomplete
    def __init__(
        self, display_name, alias, is_public, optional_params: Incomplete | None = None
    ) -> None: ...
    @property
    def entity_type_name(self) -> None: ...
