from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.service_operation import ServiceOperationPath as ServiceOperationPath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity

class TranslationJob(Entity):
    def __init__(self, context, target_language) -> None: ...
    @staticmethod
    def is_service_enabled(context, target_language): ...
    @property
    def entity_type_name(self): ...
