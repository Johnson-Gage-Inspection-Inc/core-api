from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.mount.folder_info import MountedFolderInfo as MountedFolderInfo

class MountPoint(Entity):
    @staticmethod
    def get_mounted_folder_info(context, target_site_id, target_web_id, target_unique_id): ...
