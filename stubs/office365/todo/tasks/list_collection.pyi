from _typeshed import Incomplete
from office365.delta_collection import DeltaCollection as DeltaCollection
from office365.todo.tasks.list import TodoTaskList as TodoTaskList

class TodoTaskListCollection(DeltaCollection[TodoTaskList]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, display_name): ...
