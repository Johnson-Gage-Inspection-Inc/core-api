from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.http.http_method import HttpMethod as HttpMethod
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.publishing.sites.communication.creation_request import CommunicationSiteCreationRequest as CommunicationSiteCreationRequest
from office365.sharepoint.publishing.sites.communication.creation_response import CommunicationSiteCreationResponse as CommunicationSiteCreationResponse

class CommunicationSite(Entity):
    def create(self, title, site_url, description: Incomplete | None = None): ...
    def get_status(self, site_url): ...
    def enable(self, design_package_id): ...
    @property
    def entity_type_name(self): ...
