from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity

class TranslationNotificationRecipientUsers(Entity):
    @property
    def language_code(self): ...
    @property
    def recipients(self): ...
