from _typeshed import Incomplete
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.logger.logFileInfo import LogFileInfo as LogFileInfo

class LogFileInfoCollection(EntityCollection):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
