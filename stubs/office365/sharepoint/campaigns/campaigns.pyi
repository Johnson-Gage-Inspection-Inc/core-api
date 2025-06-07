from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity

class Campaigns(Entity):
    @staticmethod
    def get_campaign(context, campaign_id): ...
