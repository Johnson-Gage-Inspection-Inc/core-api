from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity

class DocumentsSharedWithMe(Entity):
    @staticmethod
    def get_list_data(context, sort_field_name, is_ascending_sort, offset, row_limit): ...
    @property
    def entity_type_name(self): ...
