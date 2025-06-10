from office365.directory.extensions.extension import Extension as Extension
from office365.directory.object import DirectoryObject as DirectoryObject
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class AdministrativeUnit(DirectoryObject):
    @property
    def display_name(self) -> str | None: ...
    @property
    def visibility(self): ...
    @property
    def members(self): ...
    @property
    def extensions(self) -> EntityCollection[Extension]: ...
