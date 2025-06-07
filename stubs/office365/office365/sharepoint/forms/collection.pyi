from _typeshed import Incomplete
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.forms.form import Form as Form

class FormCollection(EntityCollection[Form]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_by_id(self, _id): ...
    def get_by_page_type(self, form_type): ...
