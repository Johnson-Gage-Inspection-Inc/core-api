from _typeshed import Incomplete
from office365.delta_collection import DeltaCollection as DeltaCollection
from office365.directory.object import DirectoryObject as DirectoryObject
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.http.http_method import HttpMethod as HttpMethod
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from typing_extensions import Self

class DirectoryObjectCollection(DeltaCollection[DirectoryObject]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_by_ids(self, ids, types: Incomplete | None = None): ...
    def add(self, directory_object: DirectoryObject) -> Self: ...
    def get_available_extension_properties(
        self, is_synced_from_on_premises: Incomplete | None = None
    ): ...
    def remove(self, directory_object: DirectoryObject | str) -> Self: ...
    def validate_properties(
        self,
        entity_type: Incomplete | None = None,
        display_name: Incomplete | None = None,
        mail_nickname: Incomplete | None = None,
        on_behalf_of_userid: Incomplete | None = None,
    ): ...
