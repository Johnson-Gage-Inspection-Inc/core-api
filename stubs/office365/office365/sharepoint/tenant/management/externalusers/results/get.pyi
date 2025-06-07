from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.tenant.management.externalusers.collection import (
    ExternalUserCollection as ExternalUserCollection,
)

class GetExternalUsersResults(Entity):
    @property
    def total_user_count(self) -> int | None: ...
    @property
    def user_collection_position(self) -> int | None: ...
    @property
    def external_user_collection(self): ...
    @property
    def entity_type_name(self): ...
