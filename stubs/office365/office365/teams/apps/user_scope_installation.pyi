from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.teams.apps.installation import (
    TeamsAppInstallation as TeamsAppInstallation,
)
from office365.teams.chats.chat import Chat as Chat

class UserScopeTeamsAppInstallation(TeamsAppInstallation):
    @property
    def chat(self): ...
