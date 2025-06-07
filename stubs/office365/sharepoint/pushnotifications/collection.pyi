from _typeshed import Incomplete
from office365.runtime.paths.service_operation import ServiceOperationPath as ServiceOperationPath
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.pushnotifications.subscriber import PushNotificationSubscriber as PushNotificationSubscriber

class PushNotificationSubscriberCollection(EntityCollection[PushNotificationSubscriber]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_by_store_id(self, _id): ...
