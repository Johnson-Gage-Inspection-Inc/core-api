from _typeshed import Incomplete
from office365.runtime.paths.service_operation import ServiceOperationPath as ServiceOperationPath
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.webs.template import WebTemplate as WebTemplate

class WebTemplateCollection(EntityCollection[WebTemplate]):
    def __init__(self, context, resource_path: Incomplete | None = None, parent: Incomplete | None = None) -> None: ...
    def get_by_name(self, name): ...
