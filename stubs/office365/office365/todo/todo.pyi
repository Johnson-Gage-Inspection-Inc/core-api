from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.todo.tasks.list_collection import (
    TodoTaskListCollection as TodoTaskListCollection,
)

class Todo(Entity):
    @property
    def lists(self) -> TodoTaskListCollection: ...
