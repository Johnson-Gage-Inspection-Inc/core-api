from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.directory.members_info import MembersInfo as MembersInfo
from office365.sharepoint.directory.membership_result import (
    MembershipResult as MembershipResult,
)
from office365.sharepoint.directory.my_groups_result import (
    MyGroupsResult as MyGroupsResult,
)
from office365.sharepoint.directory.user import User as User
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection

class SPHelper(Entity):
    def __init__(self, context) -> None: ...
    @staticmethod
    def is_member_of(
        context: ClientContext,
        principal_name: str,
        group_id: str,
        result: ClientResult[bool] | None = None,
    ) -> ClientResult[bool]: ...
    @staticmethod
    def check_site_availability(
        context: ClientContext, site_url: str
    ) -> ClientResult[bool]: ...
    @staticmethod
    def get_membership(context, user_id): ...
    @staticmethod
    def get_members_info(
        context, group_id, row_limit, return_type: Incomplete | None = None
    ): ...
    @staticmethod
    def get_my_groups(
        context, logon_name, offset, length, return_type: Incomplete | None = None
    ): ...
    @staticmethod
    def get_members(context, group_id, return_type: Incomplete | None = None): ...
    @staticmethod
    def get_owners(
        context: ClientContext,
        group_id: str,
        return_type: EntityCollection[User] | None = None,
    ) -> SPHelper: ...
    @staticmethod
    def remove_external_members(context: ClientContext, group_id: str) -> SPHelper: ...
    @property
    def entity_type_name(self): ...
