from office365.runtime.client_result import ClientResult as ClientResult
from office365.sharepoint.files.system_object_type import FileSystemObjectType as FileSystemObjectType
from office365.sharepoint.listitems.collection import ListItemCollection as ListItemCollection
from office365.sharepoint.listitems.listitem import ListItem as ListItem
from office365.sharepoint.lists.list import List as List
from typing import Callable, IO
from typing_extensions import Self

class ListExporter:
    @staticmethod
    def export(source_list: List, destination_file: IO, include_content: bool = False, item_exported: Callable[[ListItem], None] = None) -> Self: ...
