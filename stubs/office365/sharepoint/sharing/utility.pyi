from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.sharing.user_directory_info import UserDirectoryInfo as UserDirectoryInfo

class SharingUtility(Entity):
    def __init__(self, context) -> None: ...
    @staticmethod
    def get_user_directory_info_by_email(context, email): ...
    @staticmethod
    def validate_same_user_emails(context, primary_email, other_email, principal_name): ...
