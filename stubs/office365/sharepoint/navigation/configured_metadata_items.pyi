from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class ConfiguredMetadataNavigationItem(ClientValue):
    FieldDisplayName: Incomplete
    FieldTitle: Incomplete
    FieldTypeAsString: Incomplete
    IsContentTypeField: Incomplete
    IsFolderHierarchy: Incomplete
    IsHierarchy: Incomplete
    def __init__(self, field_display_name: Incomplete | None = None, field_title: Incomplete | None = None, field_type_as_string: Incomplete | None = None, is_content_type_field: Incomplete | None = None, is_folder_hierarchy: Incomplete | None = None, is_hierarchy: Incomplete | None = None) -> None: ...

class ConfiguredMetadataNavigationItemCollection(ClientValue):
    Items: Incomplete
    def __init__(self, items: Incomplete | None = None) -> None: ...
