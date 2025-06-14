from typing import IO, Callable

from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.files.file import File as File
from office365.sharepoint.folders.folder import Folder as Folder

class MoveCopyUtil(Entity):
    @staticmethod
    def copy_file_by_path(
        context, src_path, dest_path, overwrite, options: Incomplete | None = None
    ): ...
    @staticmethod
    def copy_folder(context, src_url, dest_url, options: Incomplete | None = None): ...
    @staticmethod
    def copy_folder_by_path(
        context, src_path, dest_path, options: Incomplete | None = None
    ): ...
    @staticmethod
    def move_folder(context, src_url, dest_url, options): ...
    @staticmethod
    def move_folder_by_path(context, src_path, dest_path, options): ...
    @staticmethod
    def download_folder(
        remove_folder: Folder,
        download_file: IO,
        after_file_downloaded: Callable[[File], None] = None,
        recursive: bool = True,
    ) -> Folder: ...
