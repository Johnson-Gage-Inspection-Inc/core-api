from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.principal.type import PrincipalType as PrincipalType
from office365.sharepoint.ui.applicationpages.peoplepicker.entity_information import PickerEntityInformation as PickerEntityInformation
from office365.sharepoint.ui.applicationpages.peoplepicker.entity_information_request import PickerEntityInformationRequest as PickerEntityInformationRequest
from office365.sharepoint.ui.applicationpages.peoplepicker.query_parameters import ClientPeoplePickerQueryParameters as ClientPeoplePickerQueryParameters

class ClientPeoplePickerWebServiceInterface(Entity):
    @staticmethod
    def get_search_results_by_hierarchy(context, provider_id: Incomplete | None = None, hierarchy_node_id: Incomplete | None = None, entity_types: Incomplete | None = None, context_url: Incomplete | None = None): ...
    @staticmethod
    def client_people_picker_resolve_user(context, query_string): ...
    @staticmethod
    def client_people_picker_search_user(context, query_string, maximum_entity_suggestions: int = 100): ...
    @staticmethod
    def get_picker_entity_information(context, email_address): ...
    @property
    def entity_type_name(self): ...

class PeoplePickerWebServiceInterface(Entity):
    @staticmethod
    def get_search_results(context, search_pattern, provider_id: Incomplete | None = None, hierarchy_node_id: Incomplete | None = None, entity_types: Incomplete | None = None): ...
    @property
    def entity_type_name(self): ...
