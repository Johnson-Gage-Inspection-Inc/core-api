from office365.communications.callrecords.session import Session as Session
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class CallRecord(Entity):
    @property
    def join_web_url(self): ...
    @property
    def organizer(self): ...
    @property
    def sessions(self): ...
