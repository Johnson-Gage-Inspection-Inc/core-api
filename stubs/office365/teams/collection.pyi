from typing import Callable

from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.builder import ODataPathBuilder as ODataPathBuilder
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)
from office365.teams.operations.async_operation import (
    TeamsAsyncOperation as TeamsAsyncOperation,
)
from office365.teams.team import Team as Team
from typing_extensions import Self

class TeamCollection(EntityCollection[Team]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_all(
        self, page_size: int = None, page_loaded: Callable[[Self], None] = None
    ) -> Self: ...
    def create(self, display_name, description: Incomplete | None = None): ...
