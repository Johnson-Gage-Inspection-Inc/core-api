from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.oauth.token_response import TokenResponse as TokenResponse

class Token(Entity):
    def __init__(self, context) -> None: ...
    def acquire(self): ...
    @property
    def entity_type_name(self): ...
