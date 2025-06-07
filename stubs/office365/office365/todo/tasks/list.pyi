from office365.directory.extensions.extension import Extension as Extension
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.todo.tasks.task import TodoTask as TodoTask

class TodoTaskList(Entity):
    @property
    def display_name(self) -> str | None: ...
    @property
    def extensions(self) -> EntityCollection[Extension]: ...
    @property
    def tasks(self) -> EntityCollection[TodoTask]: ...
    @property
    def entity_type_name(self) -> None: ...
