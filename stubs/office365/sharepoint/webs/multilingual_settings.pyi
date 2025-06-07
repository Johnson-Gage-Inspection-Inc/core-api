from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.translation.notification_recipient_set_request import TranslationNotificationRecipientSetRequest as TranslationNotificationRecipientSetRequest
from office365.sharepoint.translation.notification_recipient_users import TranslationNotificationRecipientUsers as TranslationNotificationRecipientUsers

class MultilingualSettings(Entity):
    def set_notification_recipients(self, notification_recipients): ...
    @property
    def recipients(self): ...
