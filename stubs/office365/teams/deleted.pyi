from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.teams.channels.collection import ChannelCollection as ChannelCollection

class DeletedTeam(Entity):
    @property
    def channels(self) -> ChannelCollection: ...
