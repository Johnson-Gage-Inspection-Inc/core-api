from office365.onedrive.versions.base_item import BaseItemVersion as BaseItemVersion
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from typing import AnyStr

class DriveItemVersion(BaseItemVersion):
    def restore_version(self): ...
    @property
    def content(self) -> AnyStr | None: ...
    @property
    def size(self) -> int | None: ...
