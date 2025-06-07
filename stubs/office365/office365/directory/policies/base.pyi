from office365.directory.object import DirectoryObject as DirectoryObject

class PolicyBase(DirectoryObject):
    @property
    def display_name(self) -> str | None: ...
