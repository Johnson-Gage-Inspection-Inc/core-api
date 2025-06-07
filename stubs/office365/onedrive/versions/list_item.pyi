from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.listitems.field_value_set import FieldValueSet as FieldValueSet
from office365.onedrive.versions.base_item import BaseItemVersion as BaseItemVersion
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery

class ListItemVersion(BaseItemVersion):
    def restore_version(self): ...
    @property
    def fields(self) -> EntityCollection[FieldValueSet]: ...
