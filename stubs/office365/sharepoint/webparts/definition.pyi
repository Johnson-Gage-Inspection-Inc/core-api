from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.webparts.webpart import WebPart as WebPart

class WebPartDefinition(Entity):
    def close_web_part(self): ...
    def delete_web_part(self): ...
    def save_web_part_changes(self): ...
    @property
    def id(self): ...
    @property
    def web_part(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
