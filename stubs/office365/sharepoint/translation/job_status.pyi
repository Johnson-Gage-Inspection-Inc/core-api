from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.translation.job_info import TranslationJobInfo as TranslationJobInfo

class TranslationJobStatus(Entity):
    @staticmethod
    def get_all_jobs(context, return_type: Incomplete | None = None): ...
    @property
    def entity_type_name(self): ...
