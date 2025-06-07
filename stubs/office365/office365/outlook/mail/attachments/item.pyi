from office365.outlook.mail.attachments.attachment import Attachment as Attachment
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class ItemAttachment(Attachment):
    @property
    def item(self): ...
