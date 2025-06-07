from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.sites.site import Site as Site

class WebApplication(Entity):
    @staticmethod
    def lookup(context: ClientContext, request_uri: str) -> WebApplication: ...
    @property
    def outbound_mail_sender_address(self) -> str | None: ...
    @property
    def sites(self) -> EntityCollection[Site]: ...
    @property
    def entity_type_name(self): ...
