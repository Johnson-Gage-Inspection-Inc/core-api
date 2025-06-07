from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ContentTypeEntityData(ClientValue):
    Name: Incomplete
    Description: Incomplete
    Group: Incomplete
    ParentContentTypeId: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        description: Incomplete | None = None,
        group: Incomplete | None = None,
        parent_content_type_id: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
