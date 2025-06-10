from _typeshed import Incomplete
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.folders.coloring_information import (
    FolderColoringInformation as FolderColoringInformation,
)
from office365.sharepoint.folders.folder import Folder as Folder
from typing_extensions import Self

class FolderColoring(Entity):
    def create_folder(
        self,
        decoded_url,
        coloring_information=...,
        return_type: Incomplete | None = None,
    ): ...
    def stamp_color(
        self, decoded_url: str, coloring_information: FolderColoringInformation
    ) -> Self: ...
