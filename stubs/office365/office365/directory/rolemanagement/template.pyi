from office365.directory.object import DirectoryObject as DirectoryObject

class DirectoryRoleTemplate(DirectoryObject):
    @property
    def display_name(self) -> str | None: ...
    @property
    def description(self) -> str | None: ...
