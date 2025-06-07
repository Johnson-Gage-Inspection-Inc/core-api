from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.migrationcenter.common.task_entity_data import MigrationTaskEntityData as MigrationTaskEntityData

class MigrationTask(MigrationTaskEntityData):
    def __init__(self, context) -> None: ...
    @property
    def entity_type_name(self): ...
