from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.sharepoint.entity import Entity as Entity

class QueryPersonalizationData(Entity):
    def __init__(self, context, user_id) -> None: ...
