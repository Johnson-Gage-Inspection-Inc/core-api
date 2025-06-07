from office365.sharepoint.multigeo.move_job_entity_data import (
    MoveJobEntityData as MoveJobEntityData,
)

class SiteMoveJobEntityData(MoveJobEntityData):
    @property
    def entity_type_name(self): ...
