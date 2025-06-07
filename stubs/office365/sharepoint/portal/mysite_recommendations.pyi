from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity

class MySiteRecommendations(Entity):
    @staticmethod
    def follow_item(context, uri, personal_site_uri, category): ...
    @staticmethod
    def stop_following_item(context, uri, personal_site_uri, category): ...
    @property
    def entity_type_name(self): ...
