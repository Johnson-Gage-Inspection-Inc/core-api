from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.entity import Entity as Entity

class MembershipResult(Entity):
    @property
    def groups_list(self): ...
    @property
    def entity_type_name(self): ...
