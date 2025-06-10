from _typeshed import Incomplete
from office365.delta_collection import DeltaCollection as DeltaCollection
from office365.outlook.mail.folders.folder import MailFolder as MailFolder

class MailFolderCollection(DeltaCollection[MailFolder]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
