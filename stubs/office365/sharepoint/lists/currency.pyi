from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.lists.currency_information_collection import CurrencyInformationCollection as CurrencyInformationCollection

class CurrencyList(Entity):
    @staticmethod
    def get_list(context): ...
