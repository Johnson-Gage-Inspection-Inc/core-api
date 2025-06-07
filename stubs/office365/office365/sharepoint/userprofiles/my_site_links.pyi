from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class MySiteLinks(Entity):
    @staticmethod
    def get_my_site_links(context): ...
    @property
    def all_documents_link(self) -> str | None: ...
    @property
    def all_sites_link(self) -> str | None: ...
    @property
    def entity_type_name(self): ...
