from _typeshed import Incomplete
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.listitems.versions.get_parameters import (
    GetListItemVersionsParameters as GetListItemVersionsParameters,
)
from office365.sharepoint.listitems.versions.version import (
    ListItemVersion as ListItemVersion,
)

class ListItemVersionCollection(EntityCollection[ListItemVersion]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_by_id(self, id_): ...
    def get_versions(
        self,
        row_limit: Incomplete | None = None,
        sort_descending: Incomplete | None = None,
    ): ...
