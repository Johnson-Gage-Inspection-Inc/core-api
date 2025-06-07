from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.portal.home.service_context import SharePointHomeServiceContext as SharePointHomeServiceContext

class SharePointHomeServiceContextBuilder(Entity):
    def get_context(self) -> None: ...
    @property
    def entity_type_name(self): ...
