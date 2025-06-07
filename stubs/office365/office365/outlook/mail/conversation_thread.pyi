from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.outlook.mail.post import Post as Post
from office365.outlook.mail.recipient import Recipient as Recipient
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class ConversationThread(Entity):
    def reply(self, post): ...
    @property
    def cc_recipients(self): ...
    @property
    def has_attachments(self): ...
    @property
    def to_recipients(self): ...
    @property
    def posts(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
