from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.userprofiles.cross_geo_sync_user_data_batch import CrossGeoSyncUserDataBatch as CrossGeoSyncUserDataBatch

class CrossGeoSync(Entity):
    @staticmethod
    def read_full_changes_batch(context: ClientContext, targetInstanceId: str, lastRecordId: str, batchSize: str) -> ClientResult[CrossGeoSyncUserDataBatch]: ...
    @property
    def entity_type_name(self): ...
