from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.sharing.internal.types import (
    CAnonymousLinkUseLimit as CAnonymousLinkUseLimit,
)

class SharingRestrictions(Entity):
    def __init__(self, context) -> None: ...
    @property
    def anonymous_link_use_limit(self): ...
    @property
    def entity_type_name(self) -> str: ...
